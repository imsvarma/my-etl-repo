from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.etl_job import run_etl

with DAG(
    dag_id="hello_world_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    etl_task = PythonOperator(
        task_id="run_etl_job",
        python_callable=run_etl
    )
