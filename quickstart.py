from __future__ import unicode_literals
import youtube_dl

ydl = youtube_dl.YoutubeDL()
r = None
url = "https://www.youtube.com/watch?v=RgKAFK5djSk"
with ydl:
    r = ydl.extract_info(url, download=False)

options = {
    'format': 'bestaudio/best', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",      # convert to mp3
    'outtmpl': '%(title)s',        # name the file the ID of the video
    'noplaylist' : True,        # only download single song, not playlist
}
# with youtube_dl.YoutubeDL(options) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=RgKAFK5djSk'])

print r['id']