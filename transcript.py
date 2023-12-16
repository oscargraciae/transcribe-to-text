import requests
from time import sleep
import json

filename = "./audio/test1.wav"

AUTH_TOKEN = "1d232e3e98a540bdb77c8ca370bd3fe4"

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

headers = {'authorization': AUTH_TOKEN } 

response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=read_file(filename))

json = { "audio_url": response.json()['upload_url'] }
transcript_input_response = requests.post("https://api.assemblyai.com/v2/transcript", json=json, headers=headers)
transcript_id = transcript_input_response.json()['id']

# GET TRANSCRIPT
endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

response = requests.get(endpoint, headers=headers)

while response.json()['status'] != 'completed':
        sleep(5)
        print('Transcription is processing ...')
        response = requests.get(endpoint, headers=headers)

# print(response.json())
print(response.json())
print(response.json()['status'])
print(response.json()['text'])