from __future__ import annotations

import os
from io import BytesIO

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,UploadFile,File
from fastapi.responses import StreamingResponse
from rembg import remove
from PIL import Image
import io

MAX_UPLOAD_MB = int(os.getenv("MAX_UPLOAD_MB", "16"))
MAX_DIMENSION = int(os.getenv("MAX_DIMENSION", "2000"))

CORS_ORIGINS_ENV = os.getenv("CORS_ORIGINS", "")
if CORS_ORIGINS_ENV:
    CORS_ORIGINS = [origin.strip() for origin in CORS_ORIGINS_ENV.split(",") if origin.strip()]
else:
    CORS_ORIGINS = [
        "http://localhost:9001",
        "http://127.0.0.1:9001",
        "http://localhost:3000",
        "http://localhost:5500",
        "http://localhost:8000",
    ]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://removebackground-896974988513.europe-west1.run.app",
        "http://localhost:5500"
    ],
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "okay"}
@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    output = remove(image)
    buffer = io.BytesIO()
    output.save(buffer, format="PNG")
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="image/png")