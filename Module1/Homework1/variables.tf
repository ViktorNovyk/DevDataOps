variable "region" {
  description = "Region where to deploy"
  type = string
  default = "eu-west-1"
}

variable "aws_profile_name" {
  description = "Name of the aws profile for auth"
  type = string
}