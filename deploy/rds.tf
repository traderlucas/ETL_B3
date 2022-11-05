resource "aws_db_instance" "trader_data" {
  allocated_storage    = 10
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t3.micro"
  username             = "trader"
  password             = "xapiscada"
  parameter_group_name = "default.mysql5.7"
  skip_final_snapshot  = true
}