import random


def analyze_video(video_path: str):
    """Mock highlight detection — replace with real model later"""
    highlights = []
    for i in range(3):
        start = random.uniform(10, 120)
        end = start + random.uniform(3, 6)
        confidence = random.uniform(0.7, 0.95)
        highlights.append(
            {"startTime": start, "endTime": end, "confidence": confidence}
        )
    return highlights
