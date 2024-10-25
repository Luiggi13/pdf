from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Request

from routers.utils import compress

router = APIRouter()


@router.get("/pdf", tags=["PDF"], summary="Resize pdf file size", description="")
def get_pdfs(input: str, request: Request):
    return JSONResponse(content={"message": compress(input)}, headers={"X-API": "asdsa"})
