# Chatty 
**Project implemets a caht-bot that imitates Shakespeare's style** \
\
**Hope you enjoy it**

## Requirelents:

OS: MacOS, Lunix-based systems \
python = ">=3.9" \
pip \
ollama  (details: *https://ollama.ai/*)

## Local launch
~~~
# local setup:
sh app_setup.sh # wait untill mistral model to be pulled

# after setup, there should be a mistal model in the output list while running:
ollama list

# local run:
poetry run streamlit run --client.toolbarMode minimal app.py
~~~


## Local launch using docker compose
~~~
docker-compose --compatibility up
~~~