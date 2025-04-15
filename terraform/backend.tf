terraform {
  backend "s3" {
    bucket         = "p41-dev-terraform-state-rajasekhar"
    key            = "ecs/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
