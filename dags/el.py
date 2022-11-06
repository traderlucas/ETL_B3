from dataclasses import replace
import pandas as pd

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.operators.mysql_operator import MySqlOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import timedelta, datetime

s3_conn_id = "s3-conn"
bucket = "etl-b3"
now = datetime.now()
date = now.strftime("%d/%m/%Y")


def df_1():

    dfs = pd.read_html("https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-a-vista/termo/liquidacoes-antecipadas/liquidacoes-antecipadas.htm")
    df = dfs[0]
    df = df.to_csv(sep=',', index=True)
    

    s3_hook = S3Hook(aws_conn_id=s3_conn_id)

    s3_hook.load_string(df, "liquidacoes_{0}.csv".format(date), bucket_name=bucket, replace=True)


def df_2():

    dfs = pd.read_html(f"https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-a-vista/termo/posicoes-em-aberto/posicoes-em-aberto-8AA8D0CC77D179750177DF167F150965.htm?data={date}&f=0")
    df = dfs[1]
    df = df.to_csv(sep=',', index=True)
    
    s3_hook = S3Hook(aws_conn_id=s3_conn_id)

    s3_hook.load_string(df, "liquidacoes_{0}.csv".format(date), bucket_name=bucket, replace=True)


default_args = {
    "owner": "Indicium",
    "email": "lucasdub2@gmail.com",
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

main_dag = DAG(
    dag_id="intranet-EL-dag",
    default_args=default_args,
    description="Extract, load and transform data from Intranet API.",
    schedule_interval="0 3 * * *", #midnight everyday
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=600),
)

    
liquidacoes_antecipadas_termo = PythonOperator(
        task_id='liquidacoes_antecipadas_termo', 
        python_callable=df_1,
        dag=main_dag
    )

posicoes_aberto_termo = PythonOperator(
        task_id='posicoes_aberto_termo', 
        python_callable=df_2,
        dag=main_dag
    ) 


load_to_rds = MySqlOperator(
    task_id ="input_table",
    sql= "dags/sequel/SQL_load.sql",
    dag=main_dag,
    mysql_conn_id="mysql_conn"
)


[liquidacoes_antecipadas_termo, posicoes_aberto_termo] >> load_to_rds