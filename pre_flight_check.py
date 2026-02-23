import os
import sys
from config import Config

print("[RISK CHECK] Running Pre-Flight Validation...")

# Check 1: Env File
if not os.path.exists('.env'):
    print("[WARN] .env file missing. Using defaults/demo mode.")

# Check 2: Demo Mode Status
print(f"[INFO] Demo Mode: {Config.DEMO_MODE}")

if not Config.DEMO_MODE:
    if not Config.API_KEY:
        print("[FAIL] Live mode requested but API_KEY is missing.")
        sys.exit(1)
    if Config.API_KEY.startswith('sk-'):
        print("[CHECK] API Key format looks valid.")

print("[SUCCESS] Environment is ready for stakeholder demo.")
