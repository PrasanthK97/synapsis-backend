import time
from PIL import Image
from app.models.schemas import InferenceResults, SuccessResponse


def mock_ml_inference(image: Image.Image) -> tuple[InferenceResults, int]:
    # Simulated ML inference
    time.sleep(2)

    image_inference_results_data : SuccessResponse = {
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

    return image_inference_results_data  