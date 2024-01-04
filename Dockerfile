FROM chernegi/ollama-mistral:v0.1.0
WORKDIR /app

RUN apt-get update
RUN apt-get install software-properties-common -y \
&& rm -rf /var/lib/apt/lists/*

RUN apt-get update
RUN apt-get -y install python3.10
RUN apt-get -y install python3-pip
RUN pip install --upgrade pip
RUN pip install poetry

COPY poetry.lock /app/poetry.lock
COPY pyproject.toml /app/pyproject.toml
RUN poetry --no-cache install --no-root
COPY app.py /app/app.py
COPY chatty.py /app/chatty.py

ENV GIN_MODE release

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ollama serve & poetry run streamlit run --client.toolbarMode minimal /app/app.py
