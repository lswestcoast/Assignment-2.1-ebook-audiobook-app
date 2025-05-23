#!/bin/bash

echo "🔧 Setting up your eBook & Audiobook App..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  echo "📦 Creating virtual environment..."
  python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install required packages
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Create necessary folders if missing
mkdir -p ebooks
mkdir -p static/audio

# Start the Flask app
echo "🚀 Launching Flask app at http://127.0.0.1:5000 ..."
python app.py
