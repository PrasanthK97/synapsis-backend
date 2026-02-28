try:
    from typing import TypedDict  # Python 3.8+

except ImportError:
    from typing_extensions import TypedDict  # Python < 3.8

# ---- Typed Response Models ---- #

ALLOWED_EXTENSIONS: set[str] = {"png", "jpg", "jpeg", "gif", "bmp"}

class BoundingBox(TypedDict):
    x: int
    y: int
    width: int
    height: int

class Measurements(TypedDict):
    signal_a_intensity: float
    signal_b_intensity: float
    ratio: float

class InferenceResults(TypedDict):
    target_detected: bool
    confidence_score: float
    measurements: Measurements
    bounding_boxes: dict[str, BoundingBox]

class SuccessResponse(TypedDict):
    status: str
    processing_time_ms: int
    inference_results: InferenceResults

class ErrorResponse(TypedDict):
    error: str

