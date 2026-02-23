#!/bin/bash
echo "Initializing Portfolio Demo..."
python3 pre_flight_check.py
export FLASK_ENV=production
echo "Starting Server on port 5000..."
python3 app.py
