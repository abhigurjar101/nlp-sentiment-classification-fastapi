from fastapi import FastAPI, HTTPException
from app.schemas import SummarizeRequest, SummarizeResponse, SentimentRequest, SentimentResponse
from app.models.ml_model import ml_pipeline

app = FastAPI(
    title="Production NLP Microservice",
    description="High-throughput NLP API for Text Summarization, Multi-Class Sentiment Analysis, and Category Tagging.",
    version="1.0.0"
)

@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "NLP microservice is online and model is loaded."}

@app.post("/summarize", response_model=SummarizeResponse, tags=["NLP Operations"])
def summarize_text(request: SummarizeRequest):
    try:
        summary_text = ml_pipeline.summarize(
            request.text, 
            max_length=request.max_length, 
            min_length=request.min_length
        )
        return SummarizeResponse(
            summary=summary_text,
            original_length=len(request.text),
            summary_length=len(summary_text)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze", response_model=SentimentResponse, tags=["NLP Operations"])
def analyze_sentiment(request: SentimentRequest):
    try:
        res = ml_pipeline.classify_sentiment(request.text)
        return SentimentResponse(
            sentiment=res["sentiment"],
            confidence=res["confidence"],
            category=res["category"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
