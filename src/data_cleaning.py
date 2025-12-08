import pandas as pd

def clean_spotify(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df