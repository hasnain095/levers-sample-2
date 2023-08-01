# levers-sample-2
FastAPI with RabbitMQ and Celery (Public)

# FastAPI with Celery & RabbitMQ

A sample project built with FastAPI, Celery and RabbitMQ.

## Description

This project uses FastAPI to expose APIs that process tasks using Celery. RabbitMQ is used as the broker. This project implements the micro-service architecture. The first app (app1) exposes APIs that can be consumed, the second app implements variosus functionality with Celery and RabbitMQ. Both apps also have access to producers, and consumer located in connector directory to commiunicate with each other.

This project exposes two APIs:

* POST /api/v1/api/notify/
* POST /api/v1/api/notify-sync/

## Getting Started

### Dependencies

* Docker
* Docker compose

### Installing

* Simply install docker and docker compose
* Clone this repo
* cd into the directory "levers_sample-2"
* Run following command
```
docker compose up -d
```

### Executing program

* Simply run the docker command
```
docker compose up -d
```
* Then open the browser to http://localhost:8888/docs

## Authors

Hasnain Ali

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the GNU License - see the LICENSE.md file for details

