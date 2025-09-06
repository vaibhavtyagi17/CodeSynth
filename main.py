import uvicorn
from app import app

def main():
    """Run the CodeSynth web application"""
    print("Starting CodeSynth web application...")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
