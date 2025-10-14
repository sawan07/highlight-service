# 🎬 Highlight Service

FastAPI microservice for detecting highlight moments in videos.  
Part of the **CreatorVault** ecosystem — communicates with the Kotlin API Gateway on port **8080**.

---

### 🚀 Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8002
```

---

### 🧠 Endpoints

#### POST `/highlights/analyze`
Analyze a video for highlights.
```bash
curl -X POST http://localhost:8002/highlights/analyze   -H "Authorization: Bearer downstream-key"   -H "Content-Type: application/json"   -d '{"videoId": "abc123", "fileUrl": "https://cdn.test/video.mp4"}'
```

#### GET `/highlights/{videoId}`
Retrieve highlights for a given video.

---

### ⚙️ Environment Variables

| Key | Default | Description |
|-----|----------|-------------|
| `PORT` | 8002 | Service port |
| `DOWNSTREAM_KEY` | downstream-key | Shared key with Kotlin API |

---

### 🧩 Related Services
- **creatorvault-api (Kotlin)** — API Gateway  
- **video-service (Python)** — Handles YouTube downloads  

---

MIT © 2025 — CreatorVault
