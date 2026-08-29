# ML Service — Analisis Sentimen Rempang

Service Python (FastAPI) yang menyajikan model Naive Bayes hasil skripsi
**"Analisis Sentimen: Opini Publik terhadap Kebijakan Relokasi Pulau
Rempang"** sebagai REST API, sehingga bisa didemokan langsung di halaman
portofolio.

Pipeline (preprocessing, TF-IDF, SMOTE, Naive Bayes) diadaptasi langsung
dari `Notebook/Program.ipynb` pada repo
[analisis-sentiment](https://github.com/mhdtaufiq28/analisis-sentiment),
supaya hasilnya konsisten dengan penelitian aslinya.

## Menjalankan

```bash
cd ml-service
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Training model (wajib dijalankan sekali sebelum start API,
# kecuali kamu commit folder models/ ke repo)
python train.py

# Jalankan API
uvicorn app.main:app --reload --port 8000
```

Server jalan di `http://localhost:8000`. Endpoint `/health` untuk cek hidup,
dokumentasi otomatis tersedia di `http://localhost:8000/docs`.

## Endpoint

| Method | Path       | Body                          | Response                                  |
|--------|------------|--------------------------------|--------------------------------------------|
| GET    | `/health`  | -                              | `{"status": "ok"}`                          |
| POST   | `/analyze` | `{"text": "..."}`              | `{"label": "pro"\|"kontra", "confidence": 0.0-1.0}` |

Label mengikuti skema penelitian asli: **"pro"** (mendukung kebijakan
relokasi) dan **"kontra"** (menentang).

## Struktur folder

```
ml-service/
├── app/
│   ├── main.py                    # entry point FastAPI
│   ├── routers/sentiment.py       # endpoint /analyze
│   ├── services/sentiment_service.py  # load model, fungsi prediksi
│   └── ml/
│       ├── preprocessing.py       # pipeline cleaning + Sastrawi stemming
│       └── lexicon.py             # lexicon InSet untuk pelabelan otomatis
├── data/                          # dataset & resource dari repo skripsi
│   ├── DatasetRempang.csv         # 1000 tweet tentang relokasi Rempang
│   ├── positive.tsv / negative.tsv # lexicon InSet
│   └── normalization.txt / stopwords.txt / rootwords.txt
├── models/                        # hasil training (dibuat oleh train.py)
│   ├── naive_bayes_model.joblib
│   └── tfidf_vectorizer.joblib
└── train.py                       # script training
```

## Hasil training (contoh run)

```
Akurasi pada data testing : 0.7567
Cross-validation (10-fold): 0.7995 (accuracy), 0.7969 (f1-macro)
```

Sedikit berbeda dari angka 81% pada skripsi karena random state / versi
library bisa membuat hasil SMOTE & split sedikit bervariasi — pipelinenya
tetap identik dengan notebook asli.

## Integrasi dengan backend Go

Backend Go (`backend/internal/handlers/sentiment.go`) meneruskan request
dari endpoint `POST /api/analyze-sentiment` ke service ini di
`POST /analyze`. Set environment variable `PY_SERVICE_URL` di backend Go
kalau service ini di-deploy di alamat lain dari `http://localhost:8000`.

## Tentang model & dataset

Dataset (`DatasetRempang.csv`, lexicon InSet) dan seluruh resource NLP
(`normalization.txt`, `stopwords.txt`, `rootwords.txt`) disalin dari repo
skripsi [analisis-sentiment](https://github.com/mhdtaufiq28/analisis-sentiment).
Kalau dataset di repo asli diperbarui, salin ulang file-nya ke folder
`data/` di sini lalu jalankan ulang `python train.py`.
