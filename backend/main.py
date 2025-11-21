from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any, Dict

from database import db, create_document
from schemas import Consultation

app = FastAPI(title="AI & Data Analytics Company API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
async def test_connection() -> Dict[str, Any]:
    # Quick check that database is reachable
    try:
        await db.command("ping")
        status = "ok"
    except Exception as e:
        status = f"error: {e}"
    return {"status": status}


@app.post("/consultations")
async def create_consultation(payload: Consultation) -> Dict[str, Any]:
    try:
        data = payload.dict()
        inserted_id = await create_document("consultation", data)
        return {"success": True, "id": str(inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "AI & Data Analytics Company API running"}
