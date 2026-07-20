from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Store the song catalog this recommender scores against."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs ranked by fit to the user's profile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a short reason why this song matches the user's profile."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Load songs from a CSV file into a list of dictionaries.

    Uses Python's csv module (DictReader) to read each row keyed by the header.
    Numeric columns are converted so the values can be used in math later:
      - id            -> int
      - energy, tempo_bpm, valence, danceability, acousticness -> float
    Text columns (title, artist, genre, mood) are kept as strings.

    Required by src/main.py
    """
    int_fields = {"id"}
    float_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if key in int_fields:
                    song[key] = int(value)
                elif key in float_fields:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)

    return songs

# ---------------------------------------------------------------------------
# Algorithm Recipe (additive points, max ~7.0):
#   Genre    : +2.0 exact match / +1.0 same family
#   Mood     : +2.0 exact match / +1.0 same family
#   Energy   : +2.0 * (1 - |song.energy - target|)   (continuous similarity)
#   Acoustic : +1.0 when the song's texture matches likes_acoustic
# Songs in the same group get "family" half-credit (chill-lofi vibe-first).
# ---------------------------------------------------------------------------
GENRE_GROUPS = [
    {"lofi", "ambient", "jazz", "chillhop", "classical"},
    {"pop", "indie pop", "synthwave"},
    {"edm", "house", "techno"},
    {"rock", "metal"},
    {"hip hop", "r&b"},
    {"reggae", "country"},
]
MOOD_GROUPS = [
    {"chill", "relaxed", "focused", "laid-back", "calm"},
    {"happy", "euphoric", "confident"},
    {"intense", "aggressive", "energetic"},
    {"moody", "melancholic", "nostalgic", "romantic"},
]


def _same_family(a: str, b: str, groups: List[set]) -> bool:
    """Return True if a and b fall in the same genre/mood group."""
    a, b = a.lower().strip(), b.lower().strip()
    return any(a in g and b in g for g in groups)


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Score a single song against user preferences using the Algorithm Recipe.
    Required by recommend_songs() and src/main.py

    Returns (score, reasons).
    """
    score = 0.0
    reasons: List[str] = []

    fav_genre = str(user_prefs.get("genre", "")).lower().strip()
    fav_mood = str(user_prefs.get("mood", "")).lower().strip()
    target_energy = float(user_prefs.get("energy", 0.5))
    likes_acoustic = bool(user_prefs.get("likes_acoustic", False))

    genre = str(song.get("genre", "")).lower().strip()
    mood = str(song.get("mood", "")).lower().strip()
    energy = float(song.get("energy", 0.0))
    acousticness = float(song.get("acousticness", 0.0))

    # Genre: +2.0 exact, +1.0 same family
    if genre == fav_genre:
        score += 2.0
        reasons.append(f"genre match: {genre} (+2.0)")
    elif _same_family(fav_genre, genre, GENRE_GROUPS):
        score += 1.0
        reasons.append(f"related genre: {genre} ~ {fav_genre} (+1.0)")

    # Mood: +2.0 exact, +1.0 same family
    if mood == fav_mood:
        score += 2.0
        reasons.append(f"mood match: {mood} (+2.0)")
    elif _same_family(fav_mood, mood, MOOD_GROUPS):
        score += 1.0
        reasons.append(f"similar mood: {mood} ~ {fav_mood} (+1.0)")

    # Energy: +2.0 * closeness (continuous)
    closeness = max(0.0, 1.0 - abs(energy - target_energy))
    energy_points = 2.0 * closeness
    score += energy_points
    if energy_points > 0:
        reasons.append(
            f"energy fit: {energy:.2f} vs {target_energy:.2f} (+{energy_points:.2f})")

    # Acoustic: +1.0 if texture matches taste
    if (acousticness >= 0.5) == likes_acoustic:
        score += 1.0
        texture = "acoustic" if likes_acoustic else "electronic/produced"
        reasons.append(f"{texture} texture match (+1.0)")

    return round(score, 3), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Score, rank, and return the top-k songs.
    Required by src/main.py

    Returns a list of (song_dict, score, explanation).
    """
    def row(song: Dict) -> Tuple[Dict, float, str]:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "weak match for this profile"
        return song, score, explanation

    # Score every song, then rank highest-to-lowest with a new sorted list.
    scored = [row(song) for song in songs]
    return sorted(scored, key=lambda item: item[1], reverse=True)[:k]
