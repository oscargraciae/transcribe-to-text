from logging import error
from pytube import YouTube
from os import path
from pydub import AudioSegment
import pytube

# https://www.youtube.com/watch?v=C8foOu1OH3c
# https://www.youtube.com/watch?v=J8D31ilDPHA
try:
    video = pytube.YouTube('https://www.youtube.com/watch?v=C8foOu1OH3c')
    yt = video.streams.get_audio_only().download(filename='test1.mp4', output_path='./audio')

    startMin = 0
    startSec = 0

    endMin = 0
    endSec = 10

    startTime = startMin*60*1000+startSec*1000
    endTime = endMin*60*1000+endSec*1000

    song = AudioSegment.from_file('./audio/test1.mp4', 'mp4')
    song = song.set_channels(1)
    song = song[startTime:endTime]
    song.export("./audio/test1.wav", format="wav")

except error:
    print('Errot', error)
