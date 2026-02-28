from PIL import Image
from werkzeug.datastructures import FileStorage
from app.models.schemas import ALLOWED_EXTENSIONS


def allowed_file(filename: str) -> bool:
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

def validate_image_file(file: FileStorage) -> None:
    if not file.filename:
        raise ValueError("Missing filename")

    if not allowed_file(file.filename):
        raise ValueError("Invalid file extension")

    if not file.mimetype.startswith("image/"):
        raise ValueError("Invalid MIME type")

    try:
        img = Image.open(file)
        img.verify()
        file.seek(0)  # reset pointer
    except Exception:
        raise ValueError("Invalid image file")