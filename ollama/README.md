# chernegi/ollama-mistral image

*ollama-mistral docker image:https://hub.docker.com/r/ollama/ollama/tags* \
is built on top of the image declared in the Dockerfile:

~~~
docker build --tag 'ollama-mistral' .
docker run -it --name container_om -p 11434:11434 -d ollama-mistral
docker exec -it container_om ollama serve
docker exec -it container_om ollama pul mistral
docker commit container_om chernegi/ollama-mistral
~~~
