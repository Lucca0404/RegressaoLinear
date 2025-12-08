import pandas as pd

def load_spotify_raw(path="data/raw/spotify_raw.csv"):
    return pd.read_csv(path)