# Download ffmpeg from https://ffmpeg.org/download.html
# Extract the downloaded file to the same directory as this script

from pytubefix import YouTube
from pytubefix.cli import on_progress
import subprocess
import os

# Add ffmpeg bin folder to PATH temporarily
os.environ["PATH"] = os.pathsep.join(
    [
        os.environ["PATH"],
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "ffmpeg-7.1-essentials_build",
            "bin",
        ),
    ]
)

url = "https://www.youtube.com/watch?v=0tUqIHwHDEc"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ysVideo = yt.streams.get_highest_resolution(progressive=False)
ysAudio = yt.streams.get_audio_only()

# Download video and audio separately
ysVideo.download(filename="temp_video.mp4")
ysAudio.download(filename="temp_audio.mp4")

# Merge using ffmpeg
cmd = f"ffmpeg -i temp_video.mp4 -i temp_audio.mp4 -c:v copy -c:a aac final_video.mp4"
subprocess.run(cmd, shell=True)

# Clean up temporary files
os.remove("temp_video.mp4")
os.remove("temp_audio.mp4")
