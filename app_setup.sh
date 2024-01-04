# /bin/sh
pip install --upgrade pip
pip install --no-cache-dir poetry
poetry --no-cache install --no-root
curl https://ollama.ai/install.sh | sh
ollama serve & ollama pull mistral