from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

# Directory where generated eBooks and audiobooks are stored
EBOOK_FOLDER = "ebooks"
AUDIO_FOLDER = "static/audio"

# Ensure folders exist
os.makedirs(EBOOK_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route('/')
def index():
    ebooks = [f for f in os.listdir(EBOOK_FOLDER) if f.endswith(".txt")]
    return render_template('index.html', ebooks=ebooks, audio_file=None)

# Audiobook feature disabled for hosted version
# @app.route('/generate_audio', methods=['POST'])
# def generate_audio():
#     return "Audio generation is disabled in hosted version.", 501

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(EBOOK_FOLDER, filename), as_attachment=True)

# Utility: Create sample eBooks with dummy text
if not os.listdir(EBOOK_FOLDER):
    sample_books = {
        "AI_Adventure.txt": "In a world ruled by AI, a lone human fights for freedom...",
        "Mystery_of_the_Lake.txt": "The lake held secrets no one dared to reveal, until now...",
        "Galactic_Odyssey.txt": "A mission to Mars turns into a galaxy-wide chase...",
        "Whispers_in_the_Walls.txt": "Every night, the walls whispered her name...",
        "Future_Earth.txt": "The year is 3020, and Earth has evolved in unimaginable ways..."
    }
    for filename, content in sample_books.items():
        with open(os.path.join(EBOOK_FOLDER, filename), 'w') as f:
            f.write(content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
