from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Add repo root (so scripts/ can be imported)
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from scripts.hello import say_hello


default_args = {
    "owner": "airflow",
    "retries": 1,
}

with DAG(
    dag_id="hello_world_dag",
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval="@once",
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello,
    )
