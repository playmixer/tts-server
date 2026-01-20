import os
import asyncio
import torch
from fastapi import FastAPI
from fastapi.responses import FileResponse, Response
from datetime import datetime
import time

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file(
        os.getenv("TTS_MODEL"),
        local_file
    )

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

sample_rate = 24000
speaker=os.getenv("SPEAKER")

temp_audio = 'temp'

if not os.path.exists(temp_audio):
    os.makedirs(temp_audio)

def clean_temp():
    for filename in os.listdir(temp_audio):
        file_path = os.path.join(temp_audio, filename)
        last_modified = os.stat(file_path).st_mtime
        if os.path.isfile(file_path) or os.path.islink(file_path):
            if time.time() - last_modified > 10 * 60:
                os.unlink(file_path)           


app = FastAPI()

@app.get("/clean")
async def clean():
    clean_temp()
    return Response({"status": "ok"}, 200)


@app.get("/tts_to_wav")
async def tts(text: str = "", speaker: str = speaker, sample_rate: int = sample_rate):
    try:
        if text == "":
            raise Exception("text is empty")
        
        audio_path = os.path.join(temp_audio, datetime.now().strftime("%H%M%S%f")+".wav")
        audio_paths = model.save_wav(text=text,
                                speaker=speaker,
                                sample_rate=sample_rate,
                                audio_path=audio_path)
        
        return FileResponse(audio_path, media_type="audio/wav")
    except Exception as err:
        return Response({"error": str(err)}, 500)
