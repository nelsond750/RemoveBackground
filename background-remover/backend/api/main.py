from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,UploadFile,File
from fastapi.responses import StreamingResponse
from rembg import remove
from PIL import Image
import io

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://console.cloud.google.com/run/services?project=background-remover-487110",
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