"""
Lexicon InSet (Indonesian Sentiment Lexicon) — dipakai untuk memberi label
"pro"/"kontra" secara otomatis pada data training, persis seperti di
Notebook/Program.ipynb.
"""

import pandas as pd

from app.ml.preprocessing import basic_preprocess_for_lexicon


def load_lexicon_from_tsv(negative_path, positive_path) -> dict[str, float]:
    lexicon: dict[str, float] = {}

    try:
        negative_df = pd.read_csv(negative_path, sep="\t")
        for _, row in negative_df.iterrows():
            word = str(row["word"]).strip().lower()
            weight = float(row["weight"]) if pd.notna(row["weight"]) else -1.0
            processed_word = basic_preprocess_for_lexicon(word)
            if processed_word:
                lexicon[processed_word] = weight
    except FileNotFoundError:
        pass

    try:
        positive_df = pd.read_csv(positive_path, sep="\t")
        for _, row in positive_df.iterrows():
            word = str(row["word"]).strip().lower()
            weight = float(row["weight"]) if pd.notna(row["weight"]) else 1.0
            processed_word = basic_preprocess_for_lexicon(word)
            if processed_word:
                lexicon[processed_word] = weight
    except FileNotFoundError:
        pass

    return lexicon


def label_sentiment(text: str, lexicon: dict[str, float], threshold: float = 0) -> str:
    """Label 'pro' jika skor sentimen lexicon > threshold, selain itu 'kontra'."""
    if not isinstance(text, str) or not text.strip():
        return "unknown"

    words = text.lower().split()
    sentiment_score = sum(lexicon.get(word, 0) for word in words)

    return "pro" if sentiment_score > threshold else "kontra"
