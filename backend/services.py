from PIL import Image
import io
import easyocr
import json


reader = easyocr.Reader(["en"], gpu=False)


# Dummy ML extractor (you can replace with a real model)
def extract_entities(processed_text):
# Example extraction pattern
out = {}
for line in processed_text:
if "MRP" in line.upper():
out["MRP"] = line
if "EXP" in line.upper() or "EXPIRY" in line.upper():
out["Expiry"] = line
if not out:
out["message"] = "No structured entities detected"
return out




def process_image(image_bytes):
image = Image.open(io.BytesIO(image_bytes))
result = reader.readtext(image)


# Extract only text
extracted = [text for (_, text, _) in result]
return extracted
