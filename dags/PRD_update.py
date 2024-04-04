import airflow
from airflow.models import DAG
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.task_group import TaskGroup
machines=['bebour','cilaos','deb1','hp','langevin','mafate','maido','salazie','takamaka','tamarins']

with DAG(dag_id="PRD_update", start_date=days_ago(1),schedule_interval='@once',catchup=False) as dag:
  end = DummyOperator(task_id='end')
  start = DummyOperator(task_id="start")
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
