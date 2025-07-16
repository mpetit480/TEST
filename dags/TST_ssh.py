import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils.timezone import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.contrib.operators.ssh_operator import SSHOperator


args = {
    "owner": "airflow",
    "provide_context": True,
}
with DAG(dag_id="TST_ssh") as dag:
    task1 = BashOperator(
        task_id="Start",
        bash_command="hostname && ls -l /opt/airflow"
   )

    task2 = SSHOperator(
        task_id="ssh_script00",
        ssh_conn_id='ssh_bebour',
        command='uname -a'
   )

task1 >> task2
