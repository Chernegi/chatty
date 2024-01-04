# Chatty 
### Project implemets a caht-bot that imitates Shakespeare's style
### Hope you enjoy it


**Run application in Docker container [chat url: http://localhost ]:**
~~~
docker run -it --name container_app -p 80:8501 -d chernegi/app_chatty:v0.1.0
~~~

**Build Docker image locally:**
~~~
docker build --tag "chernegi/app_chatty:v0.1.0" .
~~~