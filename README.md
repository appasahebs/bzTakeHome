Django application with docker container and search keyword on database.
======================

Pre-requisites
----------------------
Install these following requirement for this project
- Docker
- Docker compose
- python 3+

## Clone the code on your local
```$ git clone git@github.com:appasahebs/bzTakeHome.git ```
```$ cd bzTakeHome ```

## Setup and Run application
For setting this application, you need to run docker componse build and up command. Which will pull repective docker images and map application code with respective directories.

```$ docker compose build ```

In this build command, mainly local docker image going to build. It has mainly following steps ... 
- Pull the remote image for python 3
- Set workdir - /code
- Copy requirements.txt for app dependancies installation 
- Install app dependancies
- And set entrypoint to - docker-entrypoint.sh

and then run containers using ...

```$ docker compose up ```

- Start containers on above build images
- bzapp container will look for db container started and up running. It will wait until its starts.
- Next, it will apply migrations
- and starts app on port - 8000

