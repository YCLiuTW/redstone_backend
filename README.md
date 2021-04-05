# FastAPI Playground
Fast-API sandbox for exploring backend knowledge.

## Features
- Launch up with docker.

### Instructions
```sh
cd docker-fastapi
docker-compose up -d # launch up docker
docker-compose start exec python bash # access into docker
docker-compose stop # stop docker

cd app
uvicorn main:app --reload #execute RESTful API server in docker env
python test_caller.py # execute testing scripts.
```