import whisper
from pytube import YouTube
import os

def download_youtube_audio(youtube_url, output_path="audio"):
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file = audio_stream.download(output_path=output_path)
    base, ext = os.path.splitext(audio_file)
    new_file = base + '.mp3'
    os.rename(audio_file, new_file)
    return new_file

def transcribe_with_whisper(audio_file_path):
    # Load the Whisper model
    model = whisper.load_model("base")

    # Load audio file and run the transcription
    result = model.transcribe(audio_file_path)
    # Save the transcription to a text file
    
    with open('testimonio-3-noreste.txt', 'w') as text_file:
        text_file.write(result["text"])

    return result

# Example usage:
youtube_url = 'https://www.youtube.com/watch?v=x04VuQe2Jng'
audio_file_path = download_youtube_audio(youtube_url)
transcription_result = transcribe_with_whisper(audio_file_path)
print(transcription_result["text"])
