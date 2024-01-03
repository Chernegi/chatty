FROM python:3.9-slim
WORKDIR /app

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY app.py /app/app.py
COPY chatty.py /app/chatty.py

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT streamlit run --client.toolbarMode minimal /app/app.py
