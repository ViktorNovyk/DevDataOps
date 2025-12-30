provider "aws" {
  profile = var.aws_profile_name
  region = var.region
}

terraform {
  backend "s3" {
  }
}