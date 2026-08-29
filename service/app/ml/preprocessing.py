"""
Pipeline preprocessing teks Bahasa Indonesia.

Diadaptasi langsung dari Notebook/Program.ipynb pada repo skripsi
(analisis-sentiment), supaya perilaku saat inference (API) identik
dengan yang dipakai saat training di notebook.
"""

import re
import string
from pathlib import Path
from functools import lru_cache

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


def load_normalization_dict(path: Path) -> dict[str, str]:
    norm_dict: dict[str, str] = {}
    if not path.exists():
        return norm_dict
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                key, value = line.strip().split(":", 1)
                norm_dict[key.strip()] = value.strip()
    return norm_dict


def load_stopwords(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with open(path, "r", encoding="utf-8") as f:
        return {line.strip().lower() for line in f if line.strip()}


def load_root_words(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with open(path, "r", encoding="utf-8") as f:
        return {line.strip().lower() for line in f if line.strip()}


@lru_cache(maxsize=1)
def get_resources():
    """Load semua resource sekali saja (di-cache) — dipakai baik saat
    training maupun saat serving lewat API."""
    norm_dict = load_normalization_dict(DATA_DIR / "normalization.txt")
    stopwords = load_stopwords(DATA_DIR / "stopwords.txt")
    root_words = load_root_words(DATA_DIR / "rootwords.txt")
    stemmer = StemmerFactory().create_stemmer()
    return norm_dict, stopwords, root_words, stemmer


def clean_text(text: str) -> str:
    """Menghapus noise dari teks: URL, mention, hashtag, emoji, angka, tanda baca."""
    if text is None or text == "":
        return ""

    text = str(text)
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = re.sub(r'www\.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)
    text = re.sub(r'#[A-Za-z0-9_]+', '', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()

    return text


def case_folding(text: str) -> str:
    if text is None or text == "":
        return ""
    return text.lower()


def tokenize_text(text: str) -> list[str]:
    if text is None or text == "":
        return []

    tokens = [token.strip() for token in text.split() if token.strip()]
    clean_tokens = []
    for token in tokens:
        token = re.sub(r'[^\w]', '', token)
        if token:
            clean_tokens.append(token)

    return clean_tokens


def normalize_text(tokens: list[str], norm_dict: dict[str, str]) -> list[str]:
    if not tokens:
        return []
    return [norm_dict.get(token, token) for token in tokens]


def remove_stopwords(tokens: list[str], stopwords_set: set[str]) -> list[str]:
    if not tokens:
        return []
    return [token for token in tokens if token not in stopwords_set]


def sastrawi_stem(word: str, root_words: set[str], stemmer) -> str:
    word = word.lower().strip()
    if root_words and word in root_words:
        return word
    stemmed = stemmer.stem(word)
    if root_words and stemmed in root_words:
        return stemmed
    return stemmed


def stem_tokens(tokens: list[str], root_words: set[str], stemmer) -> list[str]:
    if not tokens:
        return []
    return [sastrawi_stem(token, root_words, stemmer) for token in tokens]


def full_preprocess_pipeline(text: str) -> str:
    """Pipeline lengkap: dipakai untuk training DAN untuk inference API,
    supaya representasi teks yang dilihat model selalu konsisten."""
    norm_dict, stopwords, root_words, stemmer = get_resources()

    text = clean_text(text)
    text = case_folding(text)
    tokens = tokenize_text(text)
    tokens = normalize_text(tokens, norm_dict)
    tokens = remove_stopwords(tokens, stopwords)
    tokens = stem_tokens(tokens, root_words, stemmer)

    return " ".join(tokens)


def basic_preprocess_for_lexicon(text: str) -> str:
    """Preprocessing versi ringan (tanpa stemming) — dipakai untuk
    pelabelan otomatis berbasis lexicon saat training."""
    norm_dict, stopwords, _, _ = get_resources()

    text = clean_text(text)
    text = case_folding(text)
    tokens = tokenize_text(text)
    tokens = normalize_text(tokens, norm_dict)
    tokens = remove_stopwords(tokens, stopwords)

    return " ".join(tokens)
