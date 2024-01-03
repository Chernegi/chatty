# Chatty 
**Project implemets a caht-bot that imitates Shakespeare's style** \
\
**Hope you enjoy it**


## There are two options how to run the application locally

## Option 1
### Requirements:

OS: MacOS, Lunix-based systems \
python = ">=3.9" \
pip \
ollama  (details: *https://ollama.ai/*)

### Setup and run locally
~~~
# local setup:
sh app_setup.sh # wait untill mistral model to be pulled

# after setup is completed
# Mistal model should be listed using command:
ollama list

# local run:
export GIN_MODE=release & poetry run streamlit run --client.toolbarMode minimal app.py
~~~

## Option 2
### Run locally using docker compose
more details on how to run ollama in  a Docker container by *https://hub.docker.com/r/ollama/ollama/*
~~~
# run:
docker-compose --compatibility up
~~~