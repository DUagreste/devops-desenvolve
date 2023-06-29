terraform {
    required_providers {
    aws = {
        source  = "hashicorp/aws"
        version = "~> 4.0"
    }
    }
}

# Configure the AWS Provider
provider "aws" {
    region = "us-east-1"
}

provider "aws" {
    alias = "us-east-2"
    region = "us-east-2"
}

# Create a Instances
resource "aws_instance" "dev" {
    count         = 3
    ami           = "ami-053b0d53c279acc90"
    instance_type = "t2.micro"
    key_name      = var.key_name

    tags = {
        Name = "dev${count.index}"
    }

    vpc_security_group_ids = ["${aws_security_group.acesso-ssh.id}"]    
}

resource "aws_instance" "dev4" {
    ami           = "ami-053b0d53c279acc90"
    instance_type = "t2.micro"
    key_name      = var.key_name

    tags = {
        Name = "dev4"
    }

    vpc_security_group_ids = ["${aws_security_group.acesso-ssh.id}"]
    depends_on = [ aws_s3_bucket.dev4 ]
}

resource "aws_instance" "dev5" {
    ami           = var.amis["us-east-1"]
    instance_type = "t2.micro"
    key_name      = var.key_name

    tags = {
        Name = "dev5"
    }

    vpc_security_group_ids = ["${aws_security_group.acesso-ssh.id}"]
}

resource "aws_instance" "dev6" {
    ami           = var.amis["us-east-2"]
    provider      = aws.us-east-2
    instance_type = "t2.micro"
    key_name      = var.key_name

    tags = {
        Name = "dev6"
    }

    vpc_security_group_ids = ["${aws_security_group.acesso-ssh-us-east-2.id}"]
    depends_on = [ aws_dynamodb_table.dynamodb-prod ]
}

resource "aws_instance" "dev7" {
    ami           = var.amis["us-east-2"]
    provider      = aws.us-east-2
    instance_type = "t2.micro"
    key_name      = var.key_name

    tags = {
        Name = "dev7"
    }

    vpc_security_group_ids = ["${aws_security_group.acesso-ssh-us-east-2.id}"]
}


# Create a S3 - Bucket (with ACL)
resource "aws_s3_bucket" "dev4" {
    bucket = "vitorlabs-dev4"
}

resource "aws_s3_bucket_ownership_controls" "dev4" {
    bucket = aws_s3_bucket.dev4.id
    rule {
        object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_acl" "dev4" {
    depends_on = [aws_s3_bucket_ownership_controls.dev4]

    bucket = aws_s3_bucket.dev4.id
    acl    = "private"
}

# Create a database
resource "aws_dynamodb_table" "dynamodb-prod" {
    provider       = aws.us-east-2
    name           = "GameScores"
    billing_mode   = "PAY_PER_REQUEST"
    hash_key       = "UserId"
    range_key      = "GameTitle"

    attribute {
        name = "UserId"
        type = "S"
  }

    attribute {
        name = "GameTitle"
        type = "S"
  }
}