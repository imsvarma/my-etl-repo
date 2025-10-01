from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from scripts.hello import say_hello   # import your function

# Default arguments for DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG(
    dag_id="hello_world_dag",
    default_args=default_args,
    description="A simple Hello World DAG",
    schedule_interval="@daily",   # runs once a day
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    # Define Python task
    task1 = PythonOperator(
        task_id="print_hello",
        python_callable=say_hello
    )

    task1
