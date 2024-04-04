import airflow
from airflow.models import DAG
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.task_group import TaskGroup

with DAG(dag_id="TST_taskgroup", start_date=days_ago(1),schedule_interval='@once',catchup=False) as dag:
    start = DummyOperator(task_id="start")

    with TaskGroup("takamaka", tooltip="takamaka") as takamaka:
       update = SSHOperator(
        task_id="update",
        ssh_conn_id='ssh_takamaka',
        command='apt update'
       )
       upgrade = SSHOperator(
        task_id="upgrade",
        ssh_conn_id='ssh_takamaka',
        command='DEBIAN_FRONTEND=noninteractive && apt -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" dist-upgrade'
       )
       clean = SSHOperator(
        task_id="clean",
        ssh_conn_id='ssh_takamaka',
        command='apt -y clean && apt -y autoclean && apt -y autoremove'
       )
       update >> upgrade >> clean

    end = DummyOperator(task_id='end')

    start >> takamaka >> end
