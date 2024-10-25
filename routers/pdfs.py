import os
import aiofiles
from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from fastapi import Request

from utils.utils import compress

router = APIRouter()

@router.get("/pdf", tags=["PDF"], summary="Resize pdf file size", description="")
def get_pdfs(input: str, request: Request):
    return JSONResponse(content={"message": compress(input)}, headers={"X-API": "asdsa"})
    
@router.post("/pdf/upload", tags=["PDF"], summary="Upload pdf file", description="")
async def create_upload_file(file: UploadFile | None = None):
    async with aiofiles.open("./inputs/" + file.filename, 'wb') as out_file:
            while content := await file.read(1024):
                await out_file.write(content)
    compress(file.filename.split('.')[0])
    os.remove("./inputs/" + file.filename)
    if not file:
        return {"message": "fileName"}
    else:
        return {"message": "File processed successfully", "size": file.size}