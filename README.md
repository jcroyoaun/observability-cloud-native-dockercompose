# user-api
This is a repository for creating an API to perform CRUD actions on users for a Grid Dynamics internship project. Project is based on https://www.youtube.com/watch?v=GN6ICac3OXY

# Version history 
* v0.0 - Application from tutorial (https://www.youtube.com/watch?v=GN6ICac3OXY)
* v1.0 - Application moved into Docker container


## v1.1 - Application with a POC for persisting databases
*Features*
* This version includes an addition to models.py that contains the structure for a database table.
* I renamed the Users class that inherited from BaseModel 
* temporarily removed the enum types for the Users
* Commented put and delete methods to leave MVP (get and create users only)
* Added necessary libraries to connect to Database

## v2.0 - Application with Postgres and Dockerf fully integrated with Docker compose
*Features*
* Same app, same functionality, but now with Docker compose and Postgres

## v2.1 - Added CI/CD for pushing the docker image of the FastAPI (user-api) container to hub.docker.com



# Example run so far :
From the directory where project was cloned :

docker pull jcroyoaun/user-api:latest
docker compose up -d


