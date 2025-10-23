import pendulum

from airflow.sdk import DAG
from common.common_func import regist
from airflow.providers.standard.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    regist_t1 = PythonOperator(
        task_id="regist_t1",
        python_callable=regist,
        op_args=["ny", 'male', 'kr', 'seoul']
    )

    regist_t1