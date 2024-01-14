# Pilotlog

## How to build and run the project

#### Running the development environment

* `make up`

##### Rebuilding the base Docker image

* `make rebuild`

##### Stop the containers without removing them
* `make stop`

##### Stop and remove the containers
* `make down`

### Hostnames for accessing the service directly

* Local base URL: http://127.0.0.1:8000
* API documentation: http://127.0.0.1:api/docs/

## Project description

This is a REST API with a main utility endpoint ("/import") that takes an import file persisting
the file data into the system's database and returns a processed version of the imported data,
the API consistst of just some user management endpoints for features such as:
- user creation | POST ```/api/user/create/```
- user login | POST ```/api/user/token/```
- user profile updating | PUT/PATCH ```/api/user/me/```

and the main functionality endpoint:
- import data endpoint | POST ```/import/```

You can check the API documentation in detail in the provided Swagger API documentation:

![Screenshot from 2024-01-14 14-43-14](https://github.com/HenBK/pilotlog/assets/42653917/b303b5e2-cfe6-43a8-abf0-a1b3e4b3052b)

In the documentation you can directly upload an import file to test the systems' functionality as shown below:

![Screenshot from 2024-01-14 14-53-47](https://github.com/HenBK/pilotlog/assets/42653917/f30dc819-9e56-4b21-9167-be0203522fa1)

## System design

This is a fairly simple system with very few components, here is a quick overview:

Classes that compose the system:

![pilotlog-class-diagram](https://github.com/HenBK/pilotlog/assets/42653917/9cfc0eda-847c-4105-9335-5fbfd106dbfc)

Main file import interaction sequence:

![pilotlog-sequence-diagram](https://github.com/HenBK/pilotlog/assets/42653917/5214cc17-00e0-4f69-8fba-36de8c8b0f42)

