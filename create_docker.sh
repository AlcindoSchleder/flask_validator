#!/bin/bash
app="docker_flask"
docker build -t ${app} .
docker run -d -p 56733:5000 \
  --name=${app} \
  -v $PWD:/app ${app}

