# chernegi/ollama-mistral image

*ollama-mistral docker image: https://hub.docker.com/r/ollama/ollama/tags* \
is built on top of the Dockerfile:

~~~
# build locally:
docker build --tag 'ollama-mistral' .
docker run -it --name container_om -p 11434:11434 -d ollama-mistral
docker exec -it container_om ollama serve
docker exec -it container_om ollama pull mistral
docker commit container_om chernegi/ollama-mistral:v0.1.0
~~~
