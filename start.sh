#!/bin/bash

# EU Asylum Pact App - Quick Start Script
# This script will open the app in your default browser

echo "🇪🇺 Starting EU Asylum Pact Information App..."
echo ""

# Check if Python is available
if command -v python3 &> /dev/null; then
    echo "✓ Python3 found"
    
    # Start the server in background
    cd "$(dirname "$0")"
    echo "📡 Starting web server on port 8000..."
    python3 server.py &
    SERVER_PID=$!
    
    # Wait a moment for server to start
    sleep 2
    
    echo "✓ Server started (PID: $SERVER_PID)"
    echo ""
    echo "📱 Opening app in your default browser..."
    echo ""
    
    # Open browser based on OS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        open "http://localhost:8000"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        if command -v xdg-open &> /dev/null; then
            xdg-open "http://localhost:8000"
        else
            echo "Please open: http://localhost:8000"
        fi
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
        # Windows
        start "http://localhost:8000"
    else
        echo "Please open: http://localhost:8000"
    fi
    
    echo ""
    echo "✅ App is now running!"
    echo ""
    echo "To stop the server, press Ctrl+C or run:"
    echo "kill $SERVER_PID"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    # Keep script running
    wait $SERVER_PID
    
else
    echo "❌ Python3 not found!"
    echo ""
    echo "Option 1: Install Python3 from python.org"
    echo "Option 2: Double-click index.html to open directly"
    echo ""
fi
