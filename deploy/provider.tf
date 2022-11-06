provider aws {

    region = "us-east-1"
}

terraform {
    backend "s3" {
        profile        = "essentia"
        bucket         = "ETL_B3"
        key            = "ETL_B3/prod/terraform.tfstate"
        encrypt        = true
        region         = "sa-east-1"
    }
}