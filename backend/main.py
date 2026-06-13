from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.agent_router import router as agent_router
from routes.upload_router import router as upload_router
from backend.routes.downloading_router import router as downloading_router
app = FastAPI()

app.include_router(upload_router)
app.include_router(agent_router)
app.include_router(downloading_router)

@app.get("/")
def check_api():
    return {"message": "api is working"}

allowed_origins = [
    "http://localhost:3000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)