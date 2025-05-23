@echo off
echo Setting up your eBook & Audiobook App...

:: Create virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
call venv\Scripts\activate

:: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

:: Create folders if missing
if not exist ebooks mkdir ebooks
if not exist static\audio mkdir static\audio

:: Run the Flask app
echo Launching Flask app at http://127.0.0.1:5000 ...
python app.py
pause
