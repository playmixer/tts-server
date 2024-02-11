FROM python:3.8.5

WORKDIR /app

ENV TTS_MODEL=https://models.silero.ai/models/tts/ru/v4_ru.pt

COPY server.py server.py
COPY requirements.txt requirements.txt

RUN python3 -m pip install --no-cache-dir --upgrade -r requirements.txt
# RUN python3 -m pip install torch fastapi uvicorn numpy

EXPOSE 8000
CMD uvicorn server:app --host 0.0.0.0 --port 8000