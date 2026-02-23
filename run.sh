#!/bin/bash
echo "Running seed script..."
python seed_data.py
echo"
echo "Starting Flask server..."
python app.py
