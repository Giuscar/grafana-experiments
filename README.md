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


3. **Access Grafana**
   
   Once the containers are running, navigate to the following URL in your browser to access the Grafana dashboard:
   http://127.0.0.1:3000
   The default Grafana credentials are:
   
   **Username**: admin 

   **Password**: admin (You’ll be prompted to change this upon first login)


4. **Explore the dashboards**
- Example Grafana Dashboard: below is an example of a Grafana dashboard visualized using the Infinity and Business Chart plugins.

![Example of grafana dashboard using infinity and business chart plugin](./images/dashboard.png)
- Dynamic Filter Application: the dashboard supports dynamic adaptation based on the hw_type_keys filter. This allows you to adjust the view of the metrics based on the selected filter.

![Filters applied on the graph](./images/filter.png)
