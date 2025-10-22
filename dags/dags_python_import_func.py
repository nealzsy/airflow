import pendulum
import os

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from common.common_func import get_sftp

with DAG(
    dag_id="dags_python_import_func.py",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    def print_env():
        print("WORKSPACE_FOLDER =", os.getenv("WORKSPACE_FOLDER"))
        print("PYTHONPATH =", os.getenv("PYTHONPATH"))

    print_env_task = PythonOperator(
        task_id="print_env_task",
        python_callable=print_env,
        dag=dag
    )
    task_get_sftp = PythonOperator(
        task_id="task_get_sftp",
        ptyhon_callable=get_sftp
    )


    print_env_task >> task_get_sftp