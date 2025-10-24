import pendulum

from airflow.sdk import DAG, task
from airflow.providers.standard.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_show_templates",
    schedule='30 9 * * *',
    start_date=pendulum.datetime(2025, 10, 10, tz="Asia/Seoul"),
    catchup=True,
) as dag:

    @task(task_id="python_task")
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)

    show_templates()


