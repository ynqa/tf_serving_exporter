#!/bin/bash

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build -t ynqa/tensorflow-servimg-exporter:latest
docker push ynqa/tensorflow-servimg-exporter:latest
