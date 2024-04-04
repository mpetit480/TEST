import airflow
from airflow.models import DAG
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy import DummyOperator
jobyy=""
with DAG(dag_id="Aloop", start_date=days_ago(1),schedule_interval='@once',catchup=False) as dag:
  end = DummyOperator(task_id="end")
  start = DummyOperator(task_id="start")
  mylimit=11
  for x in range(1,mylimit):
    for y in range(0,mylimit):
       a=str(x)+str(y)
       a=f"{x:0>4}"
       b=f"{y:0>4}"
       yy=a+b
       jobprev=jobyy
       jobyy = BashOperator(
              task_id="job"+yy,
              bash_command="date",
              )

       if y == 0:
           start >> jobyy 
       elif y == mylimit-1:
           jobprev >> jobyy >> end
       else:
           jobprev >> jobyy
