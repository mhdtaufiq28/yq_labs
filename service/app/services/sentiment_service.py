"""
Service untuk memuat model & vectorizer hasil training, lalu menyediakan
fungsi prediksi sentimen untuk teks baru.
"""

from pathlib import Path
from functools import lru_cache

import joblib

from app.ml.preprocessing import full_preprocess_pipeline

MODELS_DIR = Path(__file__).resolve().parent.parent.parent / "models"


class ModelNotTrainedError(RuntimeError):
    """Dilempar ketika file model belum ada (train.py belum dijalankan)."""


@lru_cache(maxsize=1)
def _load_artifacts():
    model_path = MODELS_DIR / "naive_bayes_model.joblib"
    vectorizer_path = MODELS_DIR / "tfidf_vectorizer.joblib"

    if not model_path.exists() or not vectorizer_path.exists():
        raise ModelNotTrainedError(
            "Model belum di-training. Jalankan `python train.py` terlebih dahulu."
        )

    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer


def predict_sentiment(text: str) -> dict:
    """Mengembalikan {'label': 'pro'|'kontra', 'confidence': float}."""
    model, vectorizer = _load_artifacts()

    clean = full_preprocess_pipeline(text)
    features = vectorizer.transform([clean])

    label = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    class_index = list(model.classes_).index(label)
    confidence = float(probabilities[class_index])

    return {"label": str(label), "confidence": round(confidence, 4)}
