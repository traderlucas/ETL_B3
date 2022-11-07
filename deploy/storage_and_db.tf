resource "aws_db_instance" "trader_data" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0"
  identifier           = "etl-b3"
  instance_class       = "db.t3.micro"
  username             = var.DB_USER
  password             = var.DB_PASSWORD
  port                 = "3306"
  publicly_accessible  = true
}

resource "aws_s3_bucket" "etl-b3" {
  
  bucket = "etl-b3"
  region = "us-east-1"

}