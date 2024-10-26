import os
import aiofiles
from fastapi import APIRouter, Depends, File, UploadFile

from utils.pdf_b64 import toFile
from utils.utils import compress, valid_content_length

router = APIRouter()

@router.post("/pdf/upload", dependencies=[Depends(valid_content_length)], tags=["PDF"], summary="Upload pdf file", description="")
async def create_upload_file(file: UploadFile = File(...)):
    with aiofiles.open("./inputs/" + file.filename, 'wb') as out_file:
        while content := await file.read(1024):
            await out_file.write(content)
    pdfNameCompressed = compress(file.filename.split('.')[0])
    os.remove("./inputs/" + file.filename)
    if not file:
        return {"message": "fileName"}
    else:
        return {"message": "File processed successfully", "size": pdfNameCompressed}

@router.post("/pdf/b64", tags=["PDF"], summary="Upload pdf file", description="")
async def create_upload_file(file: str):
    pdfNameCompressed = toFile(file)
    return {"message": "File processed successfully", "size": pdfNameCompressed}