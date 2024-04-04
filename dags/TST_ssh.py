rimport airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from airflow.contrib.operators.ssh_operator import SSHOperator

args = {
    "owner": "airflow",
    "provide_context": True,
}
with DAG(dag_id="TST_ssh", schedule_interval='@once', start_date=days_ago(1), default_args=args, catchup=False) as dag:
    task1 = BashOperator(
        task_id="Start",
        bash_command="echo Start"
   )

    task2 = SSHOperator(
        task_id="ssh_script00",
        ssh_conn_id='ssh_bebour',
        command='uname -a'
   )

task1 >> task2
