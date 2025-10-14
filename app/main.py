from fastapi import FastAPI, Header, HTTPException
from app.models import AnalyzeRequest, HighlightsResponse, Highlight
from app.analyzer import analyze_video

app = FastAPI(title="Highlight Service")

DOWNSTREAM_KEY = "downstream-key"


@app.post("/highlights/analyze", response_model=HighlightsResponse)
def analyze(req: AnalyzeRequest, authorization: str = Header(...)):
    if authorization != f"Bearer {DOWNSTREAM_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    items = [Highlight(**h) for h in analyze_video(req.fileUrl)]
    return HighlightsResponse(videoId=req.videoId, items=items)


@app.get("/highlights/{video_id}", response_model=HighlightsResponse)
def get_highlights(video_id: str, authorization: str = Header(...)):
    if authorization != f"Bearer {DOWNSTREAM_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Mock response
    dummy = [Highlight(startTime=12.5, endTime=17.9, confidence=0.9)]
    return HighlightsResponse(videoId=video_id, items=dummy)
