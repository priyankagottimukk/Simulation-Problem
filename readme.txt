1) info and steps to run

Web framework : Python Flask
Storage: SQlite (i'm using this because of it's portability and quick prototyping) sqlite3 is a default pckage in linux, if you need to setup for any other platform follow this steps https://www.sqlite.org/quickstart.html

Need docker tools to buld and run this image, https://docs.docker.com/docker-for-mac/

This folder contains a dockerfile used to build the docker image and a flask app and supporting classes.

when the contianer is up it will create a sqlite db object where our chat data is stored. 

Remember that object lives until the life of container, this is a limitation and we can overcome this by having a standalone DB.

Build:

1) Extract the zip and `cd chat_proj`

2) `docker build -t chat_proj .`

3) run the flask server using `docker run -p 5000:5000 chat_proj`


limitations:

For simple demo puprpose i'm using flask devlopment web server, 
if we want to run a production grade sytem we need to use WSGI servers like gunicorn.

There is no Authentication.

Better schema design can be achived by user table and messages table.

There can be better field validation and better logging

Scaling:

This approach is horizontally scalable all you need is to seperate db and scale the number of containers based on the load.


Time take: 2 hrs

More time i would have written in django with a better NoSql Database suitable for chat applications.
 


 Test commands used:

 curl --header "Content-Type: application/json" -X POST --data '{"username":"abc", "text": "hello", "timeout": 30000}' localhost:5000/chat

 curl localhost:5000/chats/abc

 curl localhost:5000/chat/61e06d0d