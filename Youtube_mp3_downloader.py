import yt_dlp
import os

# NOTE:
# FFmpeg is required for converting the downloaded audio to MP3.
#
# If FFmpeg is already added to your system PATH,
# you do not need to change anything.
#
# If FFmpeg is NOT added to your system PATH,
# add the following line inside the options dictionary:
#
# "ffmpeg_location": r"C:\path\to\your\ffmpeg\bin",
#
# Replace the path above with the location of the "bin"
# folder of FFmpeg on your own computer.
#
# Example:
# "ffmpeg_location": r"C:\ffmpeg\bin",


# Create downloads folder
os.makedirs("downloads", exist_ok=True)

url = input("Enter Any URL: ").strip()

# Check if URL is empty
if not url:
    print("Please enter a valid URL.")
    exit()


# Download settings
options = {
    "format": "bestaudio/best",

    "outtmpl": "downloads/%(title)s.%(ext)s",

    "noplaylist" : True,

    "ffmpeg_location": r"ffmpeg",

    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

# Try to download
try:
    print("\nDownloading...")

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    print("\nDOWNLOAD COMPLETE!")
    print("Check the downloads folder.")

# If something goes wrong
except Exception as e:
    print("\nDOWNLOAD FAILED")
    print("Error:", e)

user_input = input("If Download Failed Press 1  Else Press Any Other Button To Exit: ")

if user_input == "1":
    options["noplaylist"]  = False
    options["noplaylist"] = True
    
# else:
#     exit()


