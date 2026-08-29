from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.sentiment_service import ModelNotTrainedError, predict_sentiment

router = APIRouter()


class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Teks yang ingin dianalisis sentimennya")


class AnalyzeResponse(BaseModel):
    label: str  # "pro" atau "kontra"
    confidence: float


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(payload: AnalyzeRequest):
    """
    Analisis sentimen teks menggunakan model Naive Bayes hasil skripsi
    (Analisis Sentimen Opini Publik terhadap Relokasi Rempang).

    Label yang dikembalikan: "pro" atau "kontra", sesuai skema label
    pada penelitian aslinya.
    """
    try:
        return predict_sentiment(payload.text)
    except ModelNotTrainedError as e:
        raise HTTPException(status_code=503, detail=str(e))
