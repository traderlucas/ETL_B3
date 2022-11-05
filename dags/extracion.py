import pandas as pd
import pymysql
from sqlalchemy import create_engine
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta, datetime
from airflow.utils.dates import days_ago
from dags.variables import URLS

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

def df_1():

    dfs = pd.read_html("https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-de-derivativos/precos-referenciais/superficie-de-volatilidade-de-dolar/")
    df = dfs[0]
    return df

def df_2():

    dfs = pd.read_html("https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-a-vista/termo/liquidacoes-antecipadas/liquidacoes-antecipadas.htm")
    df = dfs[0]
    return df

def df_3():
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")

    dfs = pd.read_html(f"https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-a-vista/termo/posicoes-em-aberto/posicoes-em-aberto-8AA8D0CC77D179750177DF167F150965.htm?data={date}&f=0")
    df = dfs[0]
    return df

#Iterar sobre duas listas uma com as funções [df_{i}], e outra com os nomes das tasks!!!!
    
curva_superficie_dolar = PythonOperator(
        task_id='superficie_dolar', 
        python_callable=df_1,
        dag=main_dag
    )

liquidacoes_antecipadas_termo = PythonOperator(
        task_id='liquidacoes_antecipadas_termo', 
        python_callable=df_2,
        dag=main_dag
    ) 

posicoes_aberto_termo = PythonOperator(
        task_id='posicoes_aberto_termo', 
        python_callable=df_3,
        dag=main_dag
    )



curva_superficie_dolar >> load_to_rds
liquidacoes_antecipadas_termo >> load_to_rds
posicoes_aberto_termo >> load_to_rds