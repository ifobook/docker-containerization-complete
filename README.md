# Docker Containerization Complete

A DevOps project demonstrating Docker containerization of a Python Flask application.

## Technologies
- Python 3.12
- Flask
- Gunicorn
- Docker

## Project Files
- app.py - Flask web application
- requirements.txt - Python dependencies
- Dockerfile - Docker image configuration
- screenshots/ - Project evidence

## Build Docker Image

docker build -t flask-docker-app:v1 .

## Run Docker Container

docker run -d --name flask-devops-container -p 8080:5000 flask-docker-app:v1

Application: http://127.0.0.1:8080

Health endpoint: http://127.0.0.1:8080/health

## Container Management

docker ps
docker logs flask-devops-container
docker stop flask-devops-container
docker start flask-devops-container
docker rm -f flask-devops-container

## Docker Optimization
- Lightweight Python Alpine image
- Docker layer caching
- Non-root application user
- pip --no-cache-dir
- Gunicorn application server

## Verification
- Flask homepage returned HTTP 200 OK.
- Health endpoint returned HTTP 200 OK.
- Docker image built successfully.
- Container lifecycle tested.
- Image disk usage: approximately 102 MB.

## Screenshots

![Flask Application](screenshots/flask-browser.png)

![Container Lifecycle](screenshots/container-lifecycle.png)

## Completed Tasks
- [x] Prepare Flask application
- [x] Author Dockerfile
- [x] Build Docker image
- [x] Run container and map ports
- [x] Manage container lifecycle
- [x] Optimize Docker image
- [x] Document project
