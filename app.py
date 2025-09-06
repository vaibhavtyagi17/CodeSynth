import os
import json
import asyncio
from typing import Dict, Any
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

try:
    from agent.graph import agent
except ImportError as e:
    print(f"Warning: Could not import agent.graph: {e}")
    agent = None

app = FastAPI(title="CodeSynth", description="AI-powered code generation platform")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create static and templates directories
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

class CodeRequest(BaseModel):
    prompt: str
    max_steps: int = 100

class CodeResponse(BaseModel):
    success: bool
    message: str
    result: Dict[str, Any] = None
    error: str = None

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the main web interface"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/generate", response_model=CodeResponse)
async def generate_code(request: CodeRequest):
    """Generate code based on user prompt"""
    try:
        if agent is None:
            return CodeResponse(
                success=False,
                message="AI agent not available",
                error="Agent module could not be loaded. Please check your environment variables and dependencies."
            )
        
        # Run the agent in a thread pool to avoid blocking
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None, 
            lambda: agent.invoke(
                {"user_prompt": request.prompt},
                {"recursion_limit": request.max_steps}
            )
        )
        
        return CodeResponse(
            success=True,
            message="Code generation completed successfully",
            result=result
        )
    except Exception as e:
        print(f"Error in generate_code: {e}")  # Debug logging
        return CodeResponse(
            success=False,
            message="Code generation failed",
            error=str(e)
        )

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "codesynth"}

@app.get("/api/test")
async def test_endpoint():
    """Test endpoint to verify API connectivity"""
    return {
        "status": "success",
        "message": "API is working",
        "agent_available": agent is not None
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
