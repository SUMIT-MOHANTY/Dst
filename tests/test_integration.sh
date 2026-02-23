#!/bin/bash
set -e
export FLASK_ENV=testing
python -m pytest --cov=app --cov-report=html
