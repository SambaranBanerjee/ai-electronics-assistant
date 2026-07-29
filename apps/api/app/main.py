from fastapi import FastAPI

app =  FastAPI(
    title="AI Electronics Recommendation API",
    version="0.1.0",
    description="Backend API for the AI Electronics Recommendation System.",
)

@app.get("/")
async def root() -> dict[str,str]:
    return {
        "message":"AI Electronics Recommendation API is running.",
    }

@app.get("/api/v1/health")
async def health_check() -> dict[str,str]:
    return {
        "status": "healthy",
    }