resource "aws_s3_bucket" "aws_s3_bucket_ucu_lec1" {
  bucket = "vnov-ucu-de-dops-lec1"
  tags = {
    description = "UCU Data Engineering Dev DataOps Lecture 1 bucket"
  }
}

resource "aws_dynamodb_table" "aws_dd_ucu_lec1" {
  name = "UserGameList"
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "UserId"
  range_key = "GameId"

  attribute {
    name = "UserId"
    type = "N"
  }

  attribute {
    name = "GameId"
    type = "N"
  }

  tags = {
    description = "UCU Data Engineering Dev DataOps Lecture 1 data storage table"
  }
}

# Region specific so searching for a proper AMI id
data "aws_ami" "aws_ami_al2023_arm" {
  owners      = ["137112412989"] # Amazon
  most_recent = true

  filter {
    name   = "name"
    values = ["al2023-ami-*-kernel-6.1-arm64"]
  }

  filter {
    name   = "architecture"
    values = ["arm64"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
  filter {
    name   = "state"
    values = ["available"]
  }
}

resource "aws_instance" "aws_ec2_ucu_lec1" {
  ami           = data.aws_ami.aws_ami_al2023_arm.id
  instance_type = "t4g.nano"

  associate_public_ip_address = false

  root_block_device {
    volume_type           = "gp3"
    volume_size           = 8
    delete_on_termination = true
  }

  key_name = null

  tags = {
    description = "UCU Data Engineering Dev DataOps Lecture 1 VM"
  }
}