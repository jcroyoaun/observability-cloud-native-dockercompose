#!/bin/bash

create_network=$(docker network create \
--driver bridge \
--subnet 182.18.0.1/24 \
--gateway 182.18.0.1 \
users-system-network)



docker run \
  -e POSTGRES_PASSWORD=docker \
  --name users-db-postgres \
  -p 5432:5432 \
  -v 'db-data:/var/lib/postgresql/data' \
  --network users-system-network \
  -d postgres

#if on mac with M1 chip run this build command :
docker buildx build --platform linux/amd64 -t user-api .

#To run the app
docker run -p 8000:8000 --platform linux/amd64 --name user-api --network users-system-network -d user-api

# 
curl -X POST http://0.0.0.0:9090/-/reload