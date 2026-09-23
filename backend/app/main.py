import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.mongodb import client


logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)

app = FastAPI(
    title="FDM Wildfire Prediction API",
    description="Backend API for the FDM Wildfire Prediction System",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_message():
    print()
    print("========================================")
    print("   FDM WILDFIRE PREDICTION SYSTEM")
    print("========================================")
    print("  Backend : FastAPI")
    print("  Database: MongoDB Atlas")
    print("  Status  : Backend started successfully")
    print("  API     : http://127.0.0.1:8000")
    print("  Docs    : http://127.0.0.1:8000/docs")
    print("========================================")
    print()


@app.get("/")
def root():
    return {
        "message": "Wildfire Prediction API is running successfully."
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Backend is working correctly."
    }


@app.get("/api/database-health")
def database_health():
    try:
        client.admin.command("ping")

        return {
            "status": "connected",
            "message": "MongoDB is connected successfully."
        }

    except Exception:
        return {
            "status": "disconnected",
            "message": "MongoDB connection failed."
        }