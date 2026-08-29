from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import sentiment

app = FastAPI(
    title="Portfolio ML Service — Analisis Sentimen Rempang",
    description="Serve model Naive Bayes hasil skripsi sebagai REST API.",
    version="0.1.0",
)

# Service ini dipanggil oleh backend Go (internal), tapi CORS dilonggarkan
# untuk memudahkan development langsung dari frontend jika diperlukan.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(sentiment.router)


@app.get("/health")
async def health():
    return {"status": "ok"}
