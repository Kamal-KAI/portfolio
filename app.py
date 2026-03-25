# app.py — Hugging Face Spaces entry point
# HF Spaces expects the main file to be app.py.
# This shim delegates to Home.py so the project structure stays clean.

import runpy, sys, os
sys.path.insert(0, os.path.dirname(__file__))
runpy.run_path("Home.py", run_name="__main__")
