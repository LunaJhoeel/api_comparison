from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Define a request body model
class SentimentRequest(BaseModel):
    text: str

# Initialize FastAPI app
app = FastAPI()

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

@app.post("/analyze")
async def analyze_sentiment(request: SentimentRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="No text provided")

    result = sentiment_pipeline(request.text)
    return result

