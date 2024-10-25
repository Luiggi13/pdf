from fastapi.middleware.cors import CORSMiddleware
from routers import pdfs
from routers.utils import compress


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
@app.get("/", include_in_schema=False)
def read_root():
    return {"mensaje": "OK"}


if __name__ == "__main__":
    print("Starting server...")