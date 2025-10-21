from airflow.sdk import DAG
import pendulum
from airflow.providers.standard.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    send_email_task = EmailOperator(
        task_id="send_email_task",
        conn_id='conn_smtp_gmail',
        to="nayo.youn@kaihealth.tech",
        subject="Airflow Email Test",
        html_content="This is a test email from Airflow.",
    )