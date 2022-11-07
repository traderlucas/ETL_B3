source .env

export DB_HOST="database-1.cyzrjh89i5m2.us-east-1.rds.amazonaws.com"
export DB_PORT="3306"
export DB_NAME="etl1"

export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

export TF_VAR_DB_USER=$DB_USER
export TF_VAR_DB_PASSWORD=$DB_PASSWORD

export TF_VAR_PROFILE="personal"
export TF_VAR_BUCKET="etl-b3"
export TF_VAR_REGION="us-east-1"