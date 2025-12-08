import pandas as pd

def load_spotify_raw(path="data/raw/dataset_raw.csv"):
    return pd.read_csv(path)