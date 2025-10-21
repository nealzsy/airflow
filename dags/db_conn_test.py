from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from datetime import datetime

with DAG(
    dag_id='test_mysql_select',
    start_date=datetime(2025, 10, 21),
    schedule_interval=None,  # 수동 실행
    catchup=False
) as dag:

    select_test = MySqlOperator(
        task_id='select_limit_10',
        mysql_conn_id='mysql_src',
        sql='SELECT * FROM embryo_image LIMIT 10;'
    )