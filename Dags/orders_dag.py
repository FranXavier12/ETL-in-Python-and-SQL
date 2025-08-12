from pendulum import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from orders_etl_logic2 import main

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="orders_full_load",
    description="Orders table ETL DAG (Pandas → MySQL via SQLAlchemy)",
    default_args=default_args,
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    run_etl = PythonOperator(
        task_id="run_etl",
        python_callable=main,
    )
