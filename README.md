# Grafana Experiments

## Overview

This project is dedicated to experimenting with Grafana, a powerful open-source platform for monitoring and observability. The repository includes configurations and scripts to set up a Grafana environment using Docker and Python.

## Features

- **Dockerized Setup**: Utilize Docker and Docker Compose for easy environment setup.
- **Python Integration**: Includes a Python script (`web_server.py`) to simulate or collect metrics.
- **Custom Metrics**: Define and visualize custom metrics using `metrics.json`.

## Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.x](https://www.python.org/downloads/)

## Setup Instructions

1. **Clone the Repository**:
   
   ```bash
   git clone https://github.com/Giuscar/grafana-experiments.git
   cd grafana-experiments

2. **Build and Start the Docker Containers**:

    ```docker
   docker-compose start --build
    ```
    This command will build and start the services defined in the docker-compose.yaml
3. **Access Grafana**: Once the containers are up and running, navigate to http://127.0.0.1:3000 in your browser to access the Grafana dashboard. 

## Python Web Server
The **web_server.py** script is designed to expose API that will be used by Grafana to retrieve data and show them on a dashboard. To run the script: 
```bash
python3 web_server.py
```

## Custom Metrics
The **metrics.json** is an example of custom metrics that can be used to show graphs on Grafana.