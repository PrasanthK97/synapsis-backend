from flask import Blueprint, request, jsonify, Response
from PIL import Image
from app.models.schemas import SuccessResponse
from app.utils.image_utils import validate_image_file
from app.services.inference import mock_ml_inference

analyze_bp = Blueprint("analyze", __name__)


@analyze_bp.route("/api/v1/analyze-image", methods=["POST"])
def process_image() -> Response:
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files["image"]

    try:
        validate_image_file(file)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    try:
        with Image.open(file) as image:
            results = mock_ml_inference(image)

        response: SuccessResponse = results
        return jsonify(response), 200

    except Exception:
        return jsonify({"error": "Internal server error"}), 500