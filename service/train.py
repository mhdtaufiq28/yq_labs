"""
Script training model analisis sentimen — mereplikasi pipeline dari
Notebook/Program.ipynb pada repo skripsi (mhdtaufiq28/analisis-sentiment):

  1. Load dataset & lexicon InSet
  2. Labeli otomatis (pro/kontra) berdasarkan skor lexicon
  3. Preprocessing penuh (cleaning, normalisasi, stopword removal, stemming Sastrawi)
  4. Ekstraksi fitur TF-IDF (1-2 gram, max 5000 fitur)
  5. Split train/test (70/30, stratified)
  6. Oversampling SMOTE pada data training
  7. Training Multinomial Naive Bayes
  8. Evaluasi (accuracy, classification report, 10-fold CV)
  9. Simpan vectorizer + model ke models/ dengan joblib

Jalankan dari root ml-service:
    python train.py
"""

import sys
from pathlib import Path

import joblib
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import KFold, cross_validate, train_test_split
from sklearn.naive_bayes import MultinomialNB

sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.ml.lexicon import label_sentiment, load_lexicon_from_tsv
from app.ml.preprocessing import basic_preprocess_for_lexicon, full_preprocess_pipeline

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
MODELS_DIR.mkdir(exist_ok=True)


def main():
    print("=== 1. Load dataset ===")
    df = pd.read_csv(DATA_DIR / "DatasetRempang.csv")
    print(f"Dataset: {len(df)} baris")

    print("\n=== 2. Load lexicon & labeli data ===")
    lexicon = load_lexicon_from_tsv(DATA_DIR / "negative.tsv", DATA_DIR / "positive.tsv")
    print(f"Lexicon: {len(lexicon):,} kata")

    df["text_for_lexicon"] = df["full_text"].apply(basic_preprocess_for_lexicon)
    df["label"] = df["text_for_lexicon"].apply(lambda x: label_sentiment(x, lexicon, threshold=0))
    print("Distribusi label:")
    print(df["label"].value_counts())

    print("\n=== 3. Preprocessing penuh (stemming) ===")
    df["clean_text"] = df["full_text"].apply(full_preprocess_pipeline)

    print("\n=== 4. TF-IDF ===")
    vectorizer = TfidfVectorizer(
        max_features=5000,
        min_df=2,
        max_df=0.95,
        stop_words=None,
        ngram_range=(1, 2),
    )
    X = vectorizer.fit_transform(df["clean_text"])
    y = df["label"]

    print("\n=== 5. Split train/test ===")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    print(f"Training: {X_train.shape[0]} sampel | Testing: {X_test.shape[0]} sampel")

    print("\n=== 6. SMOTE oversampling ===")
    smote = SMOTE(random_state=42)
    X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
    print(f"Setelah SMOTE: {pd.Series(y_train_smote).value_counts().to_dict()}")

    print("\n=== 7. Training Naive Bayes ===")
    model = MultinomialNB()
    model.fit(X_train_smote, y_train_smote)
    print(f"Kelas: {list(model.classes_)}")

    print("\n=== 8. Evaluasi ===")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Akurasi pada data testing: {accuracy:.4f}")
    print(classification_report(y_test, y_pred))

    print("Cross validation (10-fold) pada data training (setelah SMOTE)...")
    kf = KFold(n_splits=10, shuffle=True, random_state=42)
    cv_results = cross_validate(
        model, X_train_smote, y_train_smote, cv=kf,
        scoring=["accuracy", "precision_macro", "recall_macro", "f1_macro"],
    )
    for metric in ["accuracy", "precision_macro", "recall_macro", "f1_macro"]:
        scores = cv_results[f"test_{metric}"]
        print(f"  {metric:15}: {scores.mean():.4f}")

    print("\n=== 9. Simpan artifact ===")
    joblib.dump(model, MODELS_DIR / "naive_bayes_model.joblib")
    joblib.dump(vectorizer, MODELS_DIR / "tfidf_vectorizer.joblib")
    print(f"Tersimpan di {MODELS_DIR}/")


if __name__ == "__main__":
    main()
