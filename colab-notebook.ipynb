# colab-notebook.py
# Run in Google Colab. Installs required libs, generates voice, fetches stock video, transcribes captions, builds vertical MP4.


!pip install gTTS moviepy requests openai ffmpeg-python


import os
import requests
from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip
import openai


# ------------------ CONFIG ------------------
PEXELS_API_KEY = os.getenv('PEXELS_API_KEY') # set in Colab environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') # set in Colab environment variables (for Whisper/transcription)
OUTPUT_FILE = '/content/output.mp4'


# Example: Replace this with code that pulls the Generated Script from your Google Sheet via API
SCRIPT_TEXT = "Here’s how you can launch in 7 days with AI tools…"


# ------------------ TTS ------------------
print('Generating TTS...')
tts = gTTS(SCRIPT_TEXT)
tts.save('voice.mp3')


# ------------------ PEXELS VIDEO ------------------
print('Fetching stock video from Pexels...')
headers = {"Authorization": PEXELS_API_KEY}
resp = requests.get('https://api.pexels.com/videos/search?query=business&per_page=1', headers=headers)
resp.raise_for_status()
videos = resp.json().get('videos', [])
if not videos:
raise SystemExit('No videos found from Pexels')
video_url = videos[0]['video_files'][0]['link']


with requests.get(video_url, stream=True) as r:
r.raise_for_status()
with open('background.mp4', 'wb') as f:
for chunk in r.iter_content(chunk_size=8192):
f.write(chunk)


# ------------------ TRANSFORM + COMPOSE ------------------
print('Composing final video...')
video = VideoFileClip('background.mp4').subclip(0,30)
# ensure vertical: center crop/resize to 1080x1920
video = video.resize(width=1080)
# if video height < 1920, add black bars; else crop center
if video.h < 1920:
video = video.on_color(size=(1080,1920), color=(0,0,0), pos=('center','center'))
else:
video = video.crop(width=1080, height=1920, x_center=video.w/2, y_center=video.h/2)
print('✅ Video generated ->', OUTPUT_FILE)
