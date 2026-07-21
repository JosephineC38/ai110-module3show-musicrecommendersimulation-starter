# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.


Real-world recommendations can varying but typically it's a combination of collaborative filtering (other users' behavior) and content-based filtering (songs similar to the current attributes like genre and mood). It lessens both methods' weaknesses while providing a different view for both. It uses the user's history as input data to make predications on possible songs that the user might like.

Each song includes its id, title, artist, genre, energy, tempo_bpm, valence, danceability, and acousticness. My UserProfile will store a user's favorite genre, mood, target energy, and acousticness likes to best determine what they want to hear. 
My Recommender computes a score based on the closeness to user's taste profile from a number between 0 and 1. The score formula is score =  w_genre  · genre_match
       + w_mood   · mood_match
       + w_energy · energy_proximity
       + w_acoustic · acoustic_fit, where each component is multipied by a weight based on the personality of the recommender. I choose which songs to recommend based on which songs scored higher, the closer to 1 the better. However, it will prioritize songs based on content-based filtering than collaborative filtering along with considering the user's history of liked songs.

After Phase 2, my finalized "Algorithm Recipe" is 
┌─────────────────────────────────────────────────────────────────────┐
│                     🎵 ALGORITHM RECIPE                              │
│         (additive point scoring · max ≈ 7.0 · higher = better)      │
└─────────────────────────────────────────────────────────────────────┘

   USER PROFILE                         SONG
   ┌──────────────────┐                 ┌──────────────────┐
   │ favorite_genre   │                 │ genre            │
   │ favorite_mood    │  ── compare ──▶ │ mood             │
   │ target_energy    │                 │ energy           │
   │ likes_acoustic   │                 │ acousticness     │
   └──────────────────┘                 └──────────────────┘
             │                                    │
             └─────────────────┬──────────────────┘
                               ▼
        ┌──────────────────────────────────────────────┐
        │  + GENRE     exact = +2.0 | family = +1.0     │
        │  + MOOD      exact = +2.0 | family = +1.0     │
        │  + ENERGY    +2.0 × (1 − |song − target|)     │
        │  + ACOUSTIC  fit  = +1.0                       │
        └──────────────────────────────────────────────┘
                               ▼
                    ╔══════════════════════╗
                    ║   TOTAL SCORE (0–7)  ║
                    ╚══════════════════════╝
                               ▼
              sort all songs  ▼  descending by score
                               ▼
                    ┌──────────────────────┐
                    │  RETURN TOP k SONGS  │
                    └──────────────────────┘

FAMILY = same-vibe half credit:
   genre:  lofi ≈ ambient ≈ jazz ≈ chillhop ≈ classical
   mood:   chill ≈ relaxed ≈ focused ≈ laid-back

This is based off a user profile that enjoys chili lofi music with a low energy and tempo. Some potential biases is mainstream songs biases, if a song is popular it will only be recomeded because it is popular and reinforces existing taste. Futhermore, genres might be incorrectly scored like country, which is all or nothing. Additonally, there's my own view of what's considered chili lofi, which may lead me incorrectly assume some songs aren't lofi. 

====================================================

## Sample Recommendation Output with multiple profiles
Loaded songs: 17

====================================================
  TOP RECOMMENDATIONS - High-Energy Pop
  for genre=pop | mood=happy | energy=0.9 | acoustic=False
====================================================

 1. Sunrise City  -  Neon Echo
    Score: 6.84
    Reasons:
      - genre match: pop (+2.0)
      - mood match: happy (+2.0)
      - energy fit: 0.82 vs 0.90 (+1.84)
      - electronic/produced texture match (+1.0)

 2. Rooftop Lights  -  Indigo Parade
    Score: 5.72
    Reasons:
      - related genre: indie pop ~ pop (+1.0)
      - mood match: happy (+2.0)
      - energy fit: 0.76 vs 0.90 (+1.72)
      - electronic/produced texture match (+1.0)

 3. Gym Hero  -  Max Pulse
    Score: 4.94
    Reasons:
      - genre match: pop (+2.0)
      - energy fit: 0.93 vs 0.90 (+1.94)
      - electronic/produced texture match (+1.0)

 4. Pulse Reactor  -  Delta Frequency
    Score: 3.90
    Reasons:
      - similar mood: euphoric ~ happy (+1.0)
      - energy fit: 0.95 vs 0.90 (+1.90)
      - electronic/produced texture match (+1.0)

 5. Concrete Verses  -  Crown Static
    Score: 3.76
    Reasons:
      - similar mood: confident ~ happy (+1.0)
      - energy fit: 0.78 vs 0.90 (+1.76)
      - electronic/produced texture match (+1.0)

====================================================

====================================================
  TOP RECOMMENDATIONS - Chill Lofi
  for genre=lofi | mood=chill | energy=0.35 | acoustic=True
====================================================

 1. Library Rain  -  Paper Lanterns
    Score: 7.00
    Reasons:
      - genre match: lofi (+2.0)
      - mood match: chill (+2.0)
      - energy fit: 0.35 vs 0.35 (+2.00)
      - acoustic texture match (+1.0)

 2. Midnight Coding  -  LoRoom
    Score: 6.86
    Reasons:
      - genre match: lofi (+2.0)
      - mood match: chill (+2.0)
      - energy fit: 0.42 vs 0.35 (+1.86)
      - acoustic texture match (+1.0)

 3. Focus Flow  -  LoRoom
    Score: 5.90
    Reasons:
      - genre match: lofi (+2.0)
      - similar mood: focused ~ chill (+1.0)
      - energy fit: 0.40 vs 0.35 (+1.90)
      - acoustic texture match (+1.0)

 4. Spacewalk Thoughts  -  Orbit Bloom
    Score: 5.86
    Reasons:
      - related genre: ambient ~ lofi (+1.0)
      - mood match: chill (+2.0)
      - energy fit: 0.28 vs 0.35 (+1.86)
      - acoustic texture match (+1.0)

 5. Coffee Shop Stories  -  Slow Stereo
    Score: 4.96
    Reasons:
      - related genre: jazz ~ lofi (+1.0)
      - similar mood: relaxed ~ chill (+1.0)
      - energy fit: 0.37 vs 0.35 (+1.96)
      - acoustic texture match (+1.0)

====================================================

====================================================
  TOP RECOMMENDATIONS - Deep Intense Rock
  for genre=rock | mood=intense | energy=0.9 | acoustic=False
====================================================

 1. Storm Runner  -  Voltline
    Score: 6.98
    Reasons:
      - genre match: rock (+2.0)
      - mood match: intense (+2.0)
      - energy fit: 0.91 vs 0.90 (+1.98)
      - electronic/produced texture match (+1.0)

 2. Gym Hero  -  Max Pulse
    Score: 4.94
    Reasons:
      - mood match: intense (+2.0)
      - energy fit: 0.93 vs 0.90 (+1.94)
      - electronic/produced texture match (+1.0)

 3. Iron Verdict  -  Ashfall
    Score: 4.86
    Reasons:
      - related genre: metal ~ rock (+1.0)
      - similar mood: aggressive ~ intense (+1.0)
      - energy fit: 0.97 vs 0.90 (+1.86)
      - electronic/produced texture match (+1.0)

 4. Pulse Reactor  -  Delta Frequency
    Score: 2.90
    Reasons:
      - energy fit: 0.95 vs 0.90 (+1.90)
      - electronic/produced texture match (+1.0)

 5. Sunrise City  -  Neon Echo
    Score: 2.84
    Reasons:
      - energy fit: 0.82 vs 0.90 (+1.84)
      - electronic/produced texture match (+1.0)

====================================================

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

Loaded songs: 17

====================================================
  TOP RECOMMENDATIONS
  for genre=pop | mood=happy | energy=0.8
====================================================

 1. Sunrise City  -  Neon Echo
    Score: 6.96
    Reasons:
      - genre match: pop (+2.0)
      - mood match: happy (+2.0)
      - energy fit: 0.82 vs 0.80 (+1.96)
      - electronic/produced texture match (+1.0)

 2. Rooftop Lights  -  Indigo Parade
    Score: 5.92
    Reasons:
      - related genre: indie pop ~ pop (+1.0)
      - mood match: happy (+2.0)
      - energy fit: 0.76 vs 0.80 (+1.92)
      - electronic/produced texture match (+1.0)

 3. Gym Hero  -  Max Pulse
    Score: 4.74
    Reasons:
      - genre match: pop (+2.0)
      - energy fit: 0.93 vs 0.80 (+1.74)
      - electronic/produced texture match (+1.0)

 4. Concrete Verses  -  Crown Static
    Score: 3.96
    Reasons:
      - similar mood: confident ~ happy (+1.0)
      - energy fit: 0.78 vs 0.80 (+1.96)
      - electronic/produced texture match (+1.0)

 5. Night Drive Loop  -  Neon Echo
    Score: 3.90
    Reasons:
      - related genre: synthwave ~ pop (+1.0)
      - energy fit: 0.75 vs 0.80 (+1.90)
      - electronic/produced texture match (+1.0)

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



