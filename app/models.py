from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    videoId: str
    fileUrl: str


class Highlight(BaseModel):
    startTime: float
    endTime: float
    confidence: float


class HighlightsResponse(BaseModel):
    videoId: str
    items: list[Highlight]
