# /bin/sh
pip install --upgrade pip
pip install --no-cache-dir poetry
poetry --no-cache install --no-root
ollama serve & ollama pull mistral