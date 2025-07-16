import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils.timezone import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup
from airflow.providers.ssh.operators.ssh import SSHOperator

with DAG(dag_id="TST_taskgroup") as dag:
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
