@echo off
echo Smart Desktop Activity Tracker - Setup
echo =====================================
echo.

:: Check for admin privileges
NET SESSION >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: This script requires administrator privileges.
    echo Please right-click on setup.bat and select "Run as administrator".
    pause
    exit /b 1
)

echo Installing required Python packages...
echo.

:: Create Python virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment and install packages
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install pandas scikit-learn numpy seaborn matplotlib datetime random


echo.
echo Setup complete!
echo.
echo To start the application, run start.bat
echo.
pause