terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    }
  }
}

provider aws {
    region                   = "us-east-1"
    profile                  = "personal"
    shared_credentials_files = "~/.aws/credentials"
}
