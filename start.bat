@echo off
REM EU Asylum Pact App - Windows Start Script

echo ================================================
echo    EU Asylum Pact Information App
echo ================================================
echo.

REM Check for Python
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Python found
    echo.
    echo Starting web server...
    echo.
    
    REM Start Python server
    start /B python server.py
    
    REM Wait 2 seconds
    timeout /t 2 /nobreak >nul
    
    echo [OK] Server started on port 8000
    echo.
    echo Opening app in your default browser...
    echo.
    
    REM Open in default browser
    start http://localhost:8000
    
    echo ================================================
    echo  App is now running!
    echo ================================================
    echo.
    echo To stop the server, close this window or press Ctrl+C
    echo.
    
    pause
    
) else (
    echo [ERROR] Python not found!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo.
    echo OR simply double-click "index.html" to open the app
    echo.
    pause
)
