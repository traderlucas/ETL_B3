provider aws {
    region = var.REGION
}

terraform {
    backend "s3" {
        profile        = "personal"
        bucket         = "etl-b3-terraform"
        key            = "ETL_B3/prod/terraform.tfstate"
        encrypt        = true
        region         = "us-east-1"
    }
}