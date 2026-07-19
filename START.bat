@echo off
REM ====================================
REM AI Sustainability Agent - One-Click Starter
REM ====================================

echo.
echo ====================================
echo  AI Sustainability Agent
echo  Starting up...
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [1/4] Checking Python installation... OK
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo [2/4] Creating virtual environment...
    python -m venv venv
    echo       Virtual environment created!
) else (
    echo [2/4] Virtual environment found... OK
)
echo.

REM Activate virtual environment and install dependencies
echo [3/4] Installing dependencies (first time may take a few minutes)...
call venv\Scripts\activate.bat
pip install -q -r requirements_simple.txt
if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo       Dependencies installed!
echo.

REM Create data directories
if not exist "data\uploads\" mkdir data\uploads
if not exist "data\db\" mkdir data\db

REM Check if .env exists
if not exist ".env" (
    echo Creating configuration file...
    copy .env.simple .env
)

REM Start the application
echo [4/4] Starting application...
echo.
echo ====================================
echo  READY!
echo ====================================
echo.
echo  The application is starting...
echo  Your browser will open automatically
echo.
echo  If it doesn't open, go to:
echo  http://localhost:8000
echo.
echo  Press Ctrl+C to stop the application
echo ====================================
echo.

REM Start backend with auto-browser
python simple_launcher.py

pause
