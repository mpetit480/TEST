import airflow
from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.utils.timezone import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

jobyy=""
with DAG(dag_id="Aloop", start_date=datetime(2021, 1, 1),schedule_interval=@once,catchup=False) as dag:
  end = EmptyOperator(task_id="end")
  start = EmptyOperator(task_id="start")
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
