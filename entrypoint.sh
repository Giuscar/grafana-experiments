#!/bin/sh
echo "Running initial data population script..."
python scripts/scripts.py -s -g

echo "Starting web server..."
exec python web_server.py
