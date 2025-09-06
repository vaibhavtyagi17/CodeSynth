#!/usr/bin/env python3
"""
Simple startup script for CodeSynth
This script helps diagnose common issues and starts the server
"""

import os
import sys
import subprocess
from pathlib import Path

def check_environment():
    """Check if the environment is properly set up"""
    print("🔍 Checking environment...")
    
    # Check Python version
    if sys.version_info < (3, 11):
        print("❌ Python 3.11+ is required")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")
    
    # Check if .env file exists
    if not Path(".env").exists():
        print("⚠️  .env file not found")
        print("📝 Creating .env template...")
        with open(".env", "w") as f:
            f.write("GROQ_API_KEY=your_groq_api_key_here\n")
        print("✅ Created .env file. Please add your Groq API key!")
        return False
    print("✅ .env file found")
    
    # Check if GROQ_API_KEY is set
    from dotenv import load_dotenv
    load_dotenv()
    if not os.getenv("GROQ_API_KEY") or os.getenv("GROQ_API_KEY") == "your_groq_api_key_here":
        print("❌ GROQ_API_KEY not set in .env file")
        return False
    print("✅ GROQ_API_KEY is set")
    
    return True

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def start_server():
    """Start the FastAPI server"""
    print("🚀 Starting CodeSynth server...")
    try:
        import uvicorn
        from app import app
        uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Try running: pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Server error: {e}")

def main():
    print("🎯 CodeSynth Startup Script")
    print("=" * 40)
    
    if not check_environment():
        print("\n❌ Environment check failed. Please fix the issues above.")
        return
    
    print("\n✅ Environment check passed!")
    print("\n🌐 Starting server at http://localhost:8000")
    print("📋 Test endpoints:")
    print("   - http://localhost:8000 (main interface)")
    print("   - http://localhost:8000/api/health (health check)")
    print("   - http://localhost:8000/api/test (API test)")
    print("\n🛑 Press Ctrl+C to stop the server")
    print("=" * 40)
    
    start_server()

if __name__ == "__main__":
    main()
