from fastapi import FastAPI, UploadFile
from services import process_image, extract_entities


app = FastAPI()


@app.get("/")
def home():
return {"message": "CCE AI Hackathon API Running"}


@app.post("/process-image")
async def process_image_route(file: UploadFile):
image_bytes = await file.read()
processed = process_image(image_bytes)
entities = extract_entities(processed)
return {"entities": entities}
