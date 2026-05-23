
# TTS Server

This project provides a simple Text‑to‑Speech (TTS) server based on the Silero TTS models. It exposes a REST endpoint that converts supplied text into a WAV audio file.

Key features:
- Easy Docker deployment
- Supports multiple Silero TTS models
- Simple query parameter interface

## Описание проекта

Этот проект представляет собой простой сервер преобразования текста в речь (Text‑to‑Speech) на основе моделей Silero TTS. Он предоставляет REST‑API, которое принимает параметр `text` и возвращает WAV‑файл с озвучкой.

#### Run tts server
```
docker-compose up
```

#### Get link
```
http://localhost:2800/tts_to_wav?text={text_to_speach}
```

silero model list 
https://models.silero.ai/models/tts/