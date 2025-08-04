#default_consistency/main.py
from fastapi import FastAPI
from middleware.routing import router

app = FastAPI(
    title="STCC Middleware",
    version="1.0",
    description="Strict Timed Causal Consistency Middleware for Cassandra"
)

app.include_router(router, prefix="/api")
