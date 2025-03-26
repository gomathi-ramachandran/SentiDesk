import os
import pandas as pd

def save_to_csv(file, df):
    """Saves the given DataFrame to a CSV file, appending data if the file exists."""
    if os.path.exists(file) and os.path.getsize(file) > 0:
        existing_df = pd.read_csv(file)
        df = pd.concat([existing_df, df], ignore_index=True)
    df.to_csv(file, index=False, encoding="utf-8")

def load_csv(file):
    """Loads a CSV file if it exists, otherwise returns an empty DataFrame with predefined columns."""
    if os.path.exists(file) and os.path.getsize(file) > 0:
        return pd.read_csv(file)
    return pd.DataFrame(columns=["Text", "Sentiment", "Confidence"])
