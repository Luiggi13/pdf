import os
import aiofiles
from fastapi import APIRouter, Depends, File, UploadFile

from utils.utils import compress, valid_content_length

router = APIRouter()

@router.post("/pdf/upload", dependencies=[Depends(valid_content_length)], tags=["PDF"], summary="Upload pdf file", description="")
async def create_upload_file(file: UploadFile = File(...)):
    with open("./inputs/" + file.filename, 'wb') as out_file:
        async for chunk in file.iter_chunked(1024):
            out_file.write(chunk)
    pdfNameCompressed = compress(file.filename.split('.')[0])
    os.remove("./inputs/" + file.filename)
    if not file:
        return {"message": "fileName"}
    else:
        return {"message": "File processed successfully", "size": pdfNameCompressed}