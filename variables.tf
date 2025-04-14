variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "app_image" {
  description = "Docker image for the app"
  type        = string
}