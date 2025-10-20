from airflow.sdk import DAG
import datetime
import pendulum


with DAG(
    dag_id="example_complex",
    schedule_interval=None,
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=['example', 'example2', 'example3'],
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    bash_t2 = BashOperator(
        task_id='bash_t2',
        bash_command="echo $HOSTNAME",
    )

bash_t1 >> bash_t2

