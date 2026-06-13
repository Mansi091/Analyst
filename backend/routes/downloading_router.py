from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter(
    prefix="/download",
    tags=["Download"]
)

CLEANED_DIR = "cleaned_data"


@router.get("/{filename}")
def download_cleaned_file(filename: str):

    file_path = os.path.join(CLEANED_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="Cleaned file not found"
        )

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/octet-stream"
    )