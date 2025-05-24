@echo off
echo Starting your eBook & Audiobook App...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python app.py
pause
