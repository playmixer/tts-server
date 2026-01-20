FROM python:3.8.5

WORKDIR /app


COPY server.py server.py

COPY requirements.txt requirements.txt

RUN mkdir /app/model
# RUN python3 -m pip install --no-cache-dir --upgrade -r requirements.txt
RUN python3 -m pip install torch fastapi uvicorn numpy

EXPOSE 8000
CMD  ["python3", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]