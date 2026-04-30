"""
Toonify - AI Image Transformation API
FastAPI Main Application
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.app.core.config import settings
from backend.app.database import init_db
from backend.app.routers.auth import router as auth_router
from backend.app.routers.images import router as images_router
from backend.app.routers.cartoon import router as cartoon_router

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    description="AI-based Image Transformation Tool for Cartoon Effect Generation",
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

# ✅ FINAL CORS FIX (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "https://peppy-horse-28b407.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)
app.include_router(images_router)
app.include_router(cartoon_router)

# Mount static files
app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")
app.mount("/processed", StaticFiles(directory=settings.PROCESSED_DIR), name="processed")

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/", tags=["Root"])
async def root():
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "status": "running"
    }

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}