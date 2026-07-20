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


def main() -> None:
    songs = load_songs(SONGS_CSV)
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # ---- Clean terminal layout ---------------------------------------------
    print("\n" + "=" * 52)
    print("  TOP RECOMMENDATIONS")
    print(f"  for genre={user_prefs['genre']} | "
          f"mood={user_prefs['mood']} | energy={user_prefs['energy']}")
    print("=" * 52)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n {rank}. {song['title']}  -  {song['artist']}")
        print(f"    Score: {score:.2f}")
        print("    Reasons:")
        for reason in explanation.split(", "):
            print(f"      - {reason}")

    print("\n" + "=" * 52)


if __name__ == "__main__":
    main()
