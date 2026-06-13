from fastapi import APIRouter, File, UploadFile, HTTPException
import os
import uuid

router = APIRouter(
    prefix="/upload"
)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):

    filename = file.filename.lower()

    if not filename.endswith((".csv", ".xlsx", ".xls")):
        raise HTTPException(
            status_code=400,
            detail="Only csv, xlsx, xls files are allowed"
        )

    unique_filename = f"{uuid.uuid4()}_{filename}"

    UPLOAD_DIR = "uploads"
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = f"{UPLOAD_DIR}/{unique_filename}"

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    return {
        "message": "File uploaded successfully",
        "filename": unique_filename
    }