> terraform destroy -var-file="terraform.tfvars"
```txt
data.aws_ami.aws_ami_al2023_arm: Reading...
aws_dynamodb_table.aws_dd_ucu_lec1: Refreshing state... [id=UserGameList]
aws_s3_bucket.aws_s3_bucket_ucu_lec1: Refreshing state... [id=vnov-ucu-de-dops-lec1]
data.aws_ami.aws_ami_al2023_arm: Read complete after 1s [id=ami-03ea11dcc372dba17]
aws_instance.aws_ec2_ucu_lec1: Refreshing state... [id=i-093519dd63583b032]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # aws_dynamodb_table.aws_dd_ucu_lec1 will be destroyed
  - resource "aws_dynamodb_table" "aws_dd_ucu_lec1" {
      - arn                         = "arn:aws:dynamodb:eu-west-1:407257876725:table/UserGameList" -> null
      - billing_mode                = "PAY_PER_REQUEST" -> null
      - deletion_protection_enabled = false -> null
      - hash_key                    = "UserId" -> null
      - id                          = "UserGameList" -> null
      - name                        = "UserGameList" -> null
      - range_key                   = "GameId" -> null
      - read_capacity               = 0 -> null
      - region                      = "eu-west-1" -> null
      - stream_enabled              = false -> null
      - table_class                 = "STANDARD" -> null
      - tags                        = {
          - "description" = "UCU Data Engineering Dev DataOps Lecture 1 data storage table"
        } -> null
      - tags_all                    = {
          - "description" = "UCU Data Engineering Dev DataOps Lecture 1 data storage table"
        } -> null
      - write_capacity              = 0 -> null
        # (3 unchanged attributes hidden)

      - attribute {
          - name = "GameId" -> null
          - type = "N" -> null
        }
      - attribute {
          - name = "UserId" -> null
          - type = "N" -> null
        }

      - point_in_time_recovery {
          - enabled                 = false -> null
          - recovery_period_in_days = 0 -> null
        }

      - ttl {
          - enabled        = false -> null
            # (1 unchanged attribute hidden)
        }
    }

  # aws_instance.aws_ec2_ucu_lec1 will be destroyed
  - resource "aws_instance" "aws_ec2_ucu_lec1" {
      - ami                                  = "ami-03ea11dcc372dba17" -> null
      - arn                                  = "arn:aws:ec2:eu-west-1:407257876725:instance/i-093519dd63583b032" -> null
      - associate_public_ip_address          = true -> null
      - availability_zone                    = "eu-west-1b" -> null
      - disable_api_stop                     = false -> null
      - disable_api_termination              = false -> null
      - ebs_optimized                        = false -> null
      - force_destroy                        = false -> null
      - get_password_data                    = false -> null
      - hibernation                          = false -> null
      - id                                   = "i-093519dd63583b032" -> null
      - instance_initiated_shutdown_behavior = "stop" -> null
      - instance_state                       = "running" -> null
      - instance_type                        = "t4g.nano" -> null
      - ipv6_address_count                   = 0 -> null
      - ipv6_addresses                       = [] -> null
      - monitoring                           = false -> null
      - placement_partition_number           = 0 -> null
      - primary_network_interface_id         = "eni-0c44b9e0236ddd6f8" -> null
      - private_dns                          = "ip-172-31-29-24.eu-west-1.compute.internal" -> null
      - private_ip                           = "172.31.29.24" -> null
      - public_dns                           = "ec2-3-253-51-191.eu-west-1.compute.amazonaws.com" -> null
      - public_ip                            = "3.253.51.191" -> null
      - region                               = "eu-west-1" -> null
      - secondary_private_ips                = [] -> null
      - security_groups                      = [
          - "default",
        ] -> null
      - source_dest_check                    = true -> null
      - subnet_id                            = "subnet-038223e899370f52d" -> null
      - tags                                 = {
          - "description" = "UCU Data Engineering Dev DataOps Lecture 1 VM"
        } -> null
      - tags_all                             = {
          - "description" = "UCU Data Engineering Dev DataOps Lecture 1 VM"
        } -> null
      - tenancy                              = "default" -> null
      - user_data_replace_on_change          = false -> null
      - vpc_security_group_ids               = [
          - "sg-0b75069a3ac4e02ab",
        ] -> null
        # (9 unchanged attributes hidden)

      - capacity_reservation_specification {
          - capacity_reservation_preference = "open" -> null
        }

      - cpu_options {
          - core_count       = 2 -> null
          - threads_per_core = 1 -> null
            # (1 unchanged attribute hidden)
        }

      - credit_specification {
          - cpu_credits = "unlimited" -> null
        }

      - enclave_options {
          - enabled = false -> null
        }

      - maintenance_options {
          - auto_recovery = "default" -> null
        }

      - metadata_options {
          - http_endpoint               = "enabled" -> null
          - http_protocol_ipv6          = "disabled" -> null
          - http_put_response_hop_limit = 2 -> null
          - http_tokens                 = "required" -> null
          - instance_metadata_tags      = "disabled" -> null
        }

      - primary_network_interface {
          - delete_on_termination = true -> null
          - network_interface_id  = "eni-0c44b9e0236ddd6f8" -> null
        }

      - private_dns_name_options {
          - enable_resource_name_dns_a_record    = false -> null
          - enable_resource_name_dns_aaaa_record = false -> null
          - hostname_type                        = "ip-name" -> null
        }

      - root_block_device {
          - delete_on_termination = true -> null
          - device_name           = "/dev/xvda" -> null
          - encrypted             = false -> null
          - iops                  = 3000 -> null
          - tags                  = {} -> null
          - tags_all              = {} -> null
          - throughput            = 125 -> null
          - volume_id             = "vol-047bf76b17e7b61e1" -> null
          - volume_size           = 8 -> null
          - volume_type           = "gp3" -> null
            # (1 unchanged attribute hidden)
        }
    }

  # aws_s3_bucket.aws_s3_bucket_ucu_lec1 will be destroyed
  - resource "aws_s3_bucket" "aws_s3_bucket_ucu_lec1" {
      - arn                         = "arn:aws:s3:::vnov-ucu-de-dops-lec1" -> null
      - bucket                      = "vnov-ucu-de-dops-lec1" -> null
      - bucket_domain_name          = "vnov-ucu-de-dops-lec1.s3.amazonaws.com" -> null
      - bucket_region               = "eu-west-1" -> null
      - bucket_regional_domain_name = "vnov-ucu-de-dops-lec1.s3.eu-west-1.amazonaws.com" -> null
      - force_destroy               = false -> null
      - hosted_zone_id              = "Z1BKCTXD74EZPE" -> null
      - id                          = "vnov-ucu-de-dops-lec1" -> null
      - object_lock_enabled         = false -> null
      - region                      = "eu-west-1" -> null
      - request_payer               = "BucketOwner" -> null
      - tags                        = {
          - "description" = "UCU Data Engineering Dev DataOps Lecture 1 bucket"
        } -> null
      - tags_all                    = {
          - "description" = "UCU Data Engineering Dev DataOps Lecture 1 bucket"
        } -> null
        # (3 unchanged attributes hidden)

      - grant {
          - id          = "76075db2259e3e1299a63bc8a78448c3e5ef4b4c35e5dceddf46e0dcb97355f1" -> null
          - permissions = [
              - "FULL_CONTROL",
            ] -> null
          - type        = "CanonicalUser" -> null
            # (1 unchanged attribute hidden)
        }

      - server_side_encryption_configuration {
          - rule {
              - bucket_key_enabled = false -> null

              - apply_server_side_encryption_by_default {
                  - sse_algorithm     = "AES256" -> null
                    # (1 unchanged attribute hidden)
                }
            }
        }

      - versioning {
          - enabled    = false -> null
          - mfa_delete = false -> null
        }
    }

Plan: 0 to add, 0 to change, 3 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

aws_s3_bucket.aws_s3_bucket_ucu_lec1: Destroying... [id=vnov-ucu-de-dops-lec1]
aws_dynamodb_table.aws_dd_ucu_lec1: Destroying... [id=UserGameList]
aws_instance.aws_ec2_ucu_lec1: Destroying... [id=i-093519dd63583b032]
aws_s3_bucket.aws_s3_bucket_ucu_lec1: Destruction complete after 1s
aws_dynamodb_table.aws_dd_ucu_lec1: Destruction complete after 4s
aws_instance.aws_ec2_ucu_lec1: Still destroying... [id=i-093519dd63583b032, 00m10s elapsed]
aws_instance.aws_ec2_ucu_lec1: Still destroying... [id=i-093519dd63583b032, 00m20s elapsed]
aws_instance.aws_ec2_ucu_lec1: Still destroying... [id=i-093519dd63583b032, 00m30s elapsed]
aws_instance.aws_ec2_ucu_lec1: Destruction complete after 31s

Destroy complete! Resources: 3 destroyed.
```