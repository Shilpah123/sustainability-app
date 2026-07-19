"""
Simple Launcher - Starts the application with a web interface
No Docker, no complex setup required
"""
import webbrowser
import time
import subprocess
import sys
from pathlib import Path
import os

def main():
    print("\n" + "="*50)
    print("  AI Sustainability Agent")
    print("  Simple Launcher")
    print("="*50 + "\n")
    
    # Set environment
    os.environ["USE_SIMPLE_MODE"] = "true"
    
    # Check if data directories exist
    Path("data/uploads").mkdir(parents=True, exist_ok=True)
    Path("data/db").mkdir(parents=True, exist_ok=True)
    
    print("✓ Data directories ready")
    
    # Check if .env exists
    if not Path(".env").exists():
        if Path(".env.simple").exists():
            import shutil
            shutil.copy(".env.simple", ".env")
            print("✓ Configuration file created")
    
    print("\nStarting server...")
    print("This may take a few seconds...\n")
    
    # Start uvicorn server
    try:
        import uvicorn
        
        # Open browser after a short delay
        def open_browser():
            time.sleep(2)
            webbrowser.open("http://localhost:8000")
            print("\n" + "="*50)
            print("  APPLICATION RUNNING")
            print("="*50)
            print("\n  Access the application at:")
            print("  → http://localhost:8000")
            print("\n  Press Ctrl+C to stop")
            print("="*50 + "\n")
        
        from threading import Thread
        browser_thread = Thread(target=open_browser, daemon=True)
        browser_thread.start()
        
        # Start server
        uvicorn.run(
            "simple_app:app",
            host="127.0.0.1",
            port=8000,
            reload=False,
            log_level="warning"
        )
        
    except KeyboardInterrupt:
        print("\n\nShutting down gracefully...")
        print("Thank you for using AI Sustainability Agent!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        print("\nPlease check:")
        print("1. Port 8000 is not already in use")
        print("2. All dependencies are installed")
        print("3. Try running: pip install -r requirements_simple.txt")
        input("\nPress Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()
