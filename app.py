from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import torch
import torchvision.transforms as transforms
from time import sleep
import time

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])


@app.route("/api/v1/analyze-image", methods=["POST"])
def process_image():

    # def mock_ml_inference(image_data):
    #     return image_data
    file = request.files["image"]
    image = Image.open(file).convert("RGB")
    print(image)
        
    details = {
        "filename": file.filename,
        "format": image.format,  
        "mode": image.mode,     
        "width": image.size[0],
        "height": image.size[1]
    }

    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "bmp"}
    if(("." in details["filename"] and details["filename"].rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS)== False):
        
        return {"status": "Failure due to invalid file type"}
    
    print(details)
    output_json = {
                    "status": "success",
                    "processing_time_ms": 2015,
                    "inference_results": {
                                            "target_detected": True,
                                            "confidence_score": 0.98,
                                            "measurements": {
                                                "signal_a_intensity": 245.3,
                                                "signal_b_intensity": 112.8,
                                                "ratio": 0.459
                                            },
                                            "bounding_boxes": {
                                                "target_1": {"x": 120, "y": 450, "width": 80, "height": 20},
                                                "target_2": {"x": 120, "y": 550, "width": 80, "height": 20}
                                            }
                                          }
                    }
    time.sleep(2)
    return output_json

    