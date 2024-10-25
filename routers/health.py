from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health", tags=["Health"], summary="Health check", description="")
def healthcheck():
    return JSONResponse(content={"message": "Alive"})
