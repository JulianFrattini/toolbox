# toolbox

This repository contains a list of loosely connected tools used in the academic environment.

## Overview

The repository currently consists of the following elements:

* [src](./src/) : folder containing scripts, mostly Jupyter notebooks for demonstration purposes
* [data](./data/) : folder containing data, mostly mocked for demonstration purposes

## Tools

The following tools are currently available:

* [bibfile-overlap](./src/bibfile-overlap.ipynb) : a tool detecting overlapping identifiers and titles of references in a bibliography file (`.bib`) as typically used in scientific publications written in LaTeX.
* [search-string-construction](./src/search-string-construction.ipynb) : a tool generating a search string from a list of concepts, a matrix of synonyms, and a list of relevant search fields. The search string can be used in academic databases for a systematic search.
* [dockerization](./src/dockerization/) : a exeplary repository demonstrating a simple use of Docker and docker-compose to start a RESTful API realized with `fastAPI`. More importantly, it demonstates how the file-structure should look like in case the main file ([service.py](./src/dockerization/service.py)) references helper files in subordinate folders ([helper.py](./src/dockerization/src/util/helper.py)).

## Documentation

Additional information regarding purpose and use of specific tools can be found below.

### Dockerization

The [dockerization](./src/dockerization/) folder can be used to explore the proper use of docker and docker-compose to get a simple API running. There are two ways of starting the container:

1. Via Docker directly:
  1. build the image with `docker build . -t <name>:<tag> -p 8080:8000`
  2. start the container with `docker run -it <name>` (append the `sh` attribute to enter the docker shell instead of executing the command)
2. Via Docker-compose:
  1. build the image with `docker-compose build`
  2. start the container with `docker-compose run`

Once the docker container is running, you can access the service at `localhost:8080/health`