"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import os

try:
    # Works when run from the project root: python -m src.main
    from src.recommender import load_songs, recommend_songs
except ModuleNotFoundError:
    # Works when run from inside src/: python -m main
    from recommender import load_songs, recommend_songs

# Resolve data/songs.csv relative to the project root so this runs from anywhere.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SONGS_CSV = os.path.join(BASE_DIR, "data", "songs.csv")

# ---------------------------------------------------------------------------
# User taste profiles
# Each profile is a preference dictionary the scorer reads (see score_song):
#   genre          -> favorite genre (string)
#   mood           -> favorite mood (string)
#   energy         -> target energy 0.0 (calm) .. 1.0 (high)
#   likes_acoustic -> True for acoustic textures, False for electronic/produced
# Three distinct listeners so we can see how the recommender behaves for each.
# ---------------------------------------------------------------------------
PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.9,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.9,
        "likes_acoustic": False,
    },
}

# ---------------------------------------------------------------------------
# Adversarial / edge-case profiles
# These are deliberately "unfair" inputs meant to stress the scoring logic and
# reveal where it behaves in surprising ways. Each comment states the trick and
# the behavior we expect it to expose.
# ---------------------------------------------------------------------------
ADVERSARIAL_PROFILES = {
    # Empty profile: no keys at all. score_song falls back to its defaults
    # (genre="", mood="", energy=0.5, likes_acoustic=False), so nobody matches
    # genre or mood and the ranking is driven purely by "closest to mid energy +
    # electronic texture." Reveals the recommender's built-in default bias.
    "Empty Profile": {},
    # Unknown taxonomy: "polka" and "sad" don't exist in GENRE_GROUPS/MOOD_GROUPS
    # (note "sad" is NOT recognized as the same family as "melancholic"), so both
    # earn zero credit -- not even family half-credit. Only energy + acoustic
    # count. Shows how vocabulary gaps quietly degrade to generic results.
    "Unknown Taxonomy": {
        "genre": "polka",
        "mood": "sad",
        "energy": 0.5,
        "likes_acoustic": False,
    },
}


def print_recommendations(name: str, user_prefs: dict, songs: list) -> None:
    """Score the catalog for one profile and print a clean, ranked list."""
    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Use .get() so headers still render for sparse/edge-case profiles.
    print("\n" + "=" * 52)
    print(f"  TOP RECOMMENDATIONS - {name}")
    print(f"  for genre={user_prefs.get('genre', '(none)')} | "
          f"mood={user_prefs.get('mood', '(none)')} | "
          f"energy={user_prefs.get('energy', 0.5)} | "
          f"acoustic={user_prefs.get('likes_acoustic', False)}")
    print("=" * 52)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n {rank}. {song['title']}  -  {song['artist']}")
        print(f"    Score: {score:.2f}")
        print("    Reasons:")
        for reason in explanation.split(", "):
            print(f"      - {reason}")

    print("\n" + "=" * 52)


def main() -> None:
    songs = load_songs(SONGS_CSV)
    print(f"Loaded songs: {len(songs)}")

    # Only the real listener profiles run here. The edge cases in
    # ADVERSARIAL_PROFILES are kept for manual testing, not the normal run.
    for name, user_prefs in PROFILES.items():
        print_recommendations(name, user_prefs, songs)


if __name__ == "__main__":
    main()
