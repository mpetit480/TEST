import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils.timezone import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.providers.ssh.operators.ssh import SSHOperator

from airflow.utils.task_group import TaskGroup
machines=['bebour','cilaos','deb1','hp','langevin','mafate','maido','salazie','takamaka','tamarins']

with DAG(dag_id="PRD_update") as dag:
  end = EmptyOperator(task_id='end')
  start = EmptyOperator(task_id="start")
  for variable in machines:
    server=variable
    with TaskGroup(variable, tooltip=variable) as variable:
       update = SSHOperator(
        task_id="update",
        ssh_conn_id='ssh_' + server,
        command='apt update ; sleep 10'
       )
       upgrade = SSHOperator(
        task_id="upgrade",
        ssh_conn_id='ssh_' + server,
        command='DEBIAN_FRONTEND=noninteractive && apt -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" dist-upgrade'
       )
       clean = SSHOperator(
        task_id="clean",
        ssh_conn_id='ssh_'+ server,
        command='apt -y clean && apt -y autoclean && apt -y autoremove'
       )
       update >> upgrade >> clean


    start >> variable >> end
