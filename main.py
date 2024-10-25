from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import pdfs, health
from utils.utils import compress


from fastapi import FastAPI, Request

ORIGINS = ["*"]
app = FastAPI(
    title="User Management",
    description="Compression de PDFs",
    docs_url="/docs",
    redoc_url=None,
    version="1.0.0",
    contact={
        "name": "Christian Llansola",
        "email": "christian.llansola@gmail.com",
    })

app.mount("/ok", StaticFiles(directory="descargas", html = False), name="descargas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(pdfs.router)
app.include_router(health.router)
