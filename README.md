# Particle41 DevOps Challenge

This repository contains the solution for the Particle41 DevOps Team Challenge, including a SimpleTimeService application and Terraform infrastructure for AWS ECS deployment.


# SimpleTimeService

A lightweight Flask-based microservice that provides UTC timestamp and client IP address information.

## Overview

SimpleTimeService is a minimalist REST API service built with Flask that returns the current UTC timestamp and the client's IP address. The service is containerized using Docker and can be deployed to AWS ECS using Terraform.

## Technologies Used

- Python 3.x
- Flask 2.0.1
- Docker
- Terraform
- AWS ECS (Elastic Container Service)
- AWS ALB (Application Load Balancer)

## Prerequisites

- Python 3.x
- Docker
- Terraform (for AWS deployment)
- AWS CLI configured with appropriate credentials (for deployment)

## Installation

### Local Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Kasireddy28/p41-dev.git
   cd p41-dev
   ```

2. Install Python dependencies:
   ```bash
   cd app
   pip install -r requirements.txt
   ```

### Docker Setup

1. Build the Docker image:
   ```bash
   cd app
   docker build -t timeservice .
   ```

2. Run the container:
   ```bash
   docker run -d -p 8080:8080 timeservice
   ```

## Usage

### Running the Application

#### Local Development
```bash
python app/app.py
```

#### Docker Container
```bash
docker run -d -p 8080:8080 timeservice
```

### Available Endpoints

#### GET /
Returns the current UTC timestamp and client IP address.

**Example Request:**
```bash
curl http://localhost:8080/
```

**Example Response:**
```json
{
    "timestamp": "2025-04-15T08:28:20.534083",
    "ip": "127.0.0.1"
}
```

## Infrastructure Setup

### AWS Deployment with Terraform

1. Navigate to the terraform directory:
   ```bash
   cd terraform
   ```

2. Initialize Terraform:
   ```bash
   terraform init
   ```

3. Review the deployment plan:
   ```bash
   terraform plan
   ```

4. Apply the infrastructure:
   ```bash
   terraform apply
   ```

### Infrastructure Components

- VPC with public and private subnets
- ECS Fargate cluster
- Application Load Balancer
- Security Groups
- IAM roles and policies

## Development
```

### Environment Variables

- `PORT`: Application port (default: 8080)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Security

The application implements several security best practices:
- Runs as non-root user in Docker
- Uses secure HTTP headers
- Implements rate limiting
- Runs in isolated VPC when deployed to AWS

## Monitoring and Logging

When deployed to AWS:
- CloudWatch logs for container logs
- ALB access logs
- Container health checks
- ECS service metrics

## Support

For support, please open an issue in the GitHub repository.
