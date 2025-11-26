#!/usr/bin/env bash
set -e

# Create a virtual environment, install dependencies, and run the demo
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Adjust the sample image path if you uploaded a different file
python inference.py --image sample_images/test1.jpg --output output.jpg

echo "Demo finished. See output.jpg"
