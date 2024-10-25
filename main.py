from fastapi.middleware.cors import CORSMiddleware
from routers import pdfs, health
from utils.utils import compress


from fastapi import FastAPI, Request

PREFIX= "/api/v1"
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(pdfs.router,prefix=PREFIX)
app.include_router(health.router,prefix=PREFIX)
