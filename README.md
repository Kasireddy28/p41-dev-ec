# Particle41 DevOps Challenge

This repository contains the solution for the Particle41 DevOps Team Challenge, including a SimpleTimeService application and Terraform infrastructure for AWS ECS deployment.

## Task 1: SimpleTimeService

### Overview
SimpleTimeService is a Python Flask web server that responds to GET requests at `/` with a JSON object containing the current UTC timestamp and the visitor's IP address.

### Prerequisites
- **Python 3.9+**: Install from [python.org](https://www.python.org/downloads/).
- **Docker**: Install from [docker.com](https://www.docker.com/products/docker-desktop/).

### Build and Run Locally
1. Navigate to the `app/` directory:
   ```bash
   cd app