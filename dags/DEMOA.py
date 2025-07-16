import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils.timezone import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

dag = DAG(
    dag_id="DEMOA"
)

START = BashOperator(
    task_id='START',
    bash_command="echo START",
    execution_timeout=timedelta(hours=3),dag=dag)
END = BashOperator(
    task_id='END',
    bash_command="echo END ",
    execution_timeout=timedelta(hours=3),dag=dag)
j1 = BashOperator(
   task_id='j1',
   bash_command="echo j1 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j2 = BashOperator(
   task_id='j2',
   bash_command="echo j2 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j1 >>j2
j3 = BashOperator(
   task_id='j3',
   bash_command="echo j3 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j2 >>j3
j4 = BashOperator(
   task_id='j4',
   bash_command="echo j4 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j3 >>j4
j5 = BashOperator(
   task_id='j5',
   bash_command="echo j5 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j4 >>j5
j6 = BashOperator(
   task_id='j6',
   bash_command="echo j6 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j5 >>j6
j7 = BashOperator(
   task_id='j7',
   bash_command="echo j7 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j6 >>j7
j8 = BashOperator(
   task_id='j8',
   bash_command="echo j8 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j7 >>j8
j9 = BashOperator(
   task_id='j9',
   bash_command="echo j9 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j8 >>j9
j10 = BashOperator(
   task_id='j10',
   bash_command="echo j10 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j9 >>j10
j10 >> END

j12 = BashOperator(
   task_id='j12',
   bash_command="echo j12 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j13 = BashOperator(
   task_id='j13',
   bash_command="echo j13 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j12 >>j13
j14 = BashOperator(
   task_id='j14',
   bash_command="echo j14 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j13 >>j14
j15 = BashOperator(
   task_id='j15',
   bash_command="echo j15 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j14 >>j15
j16 = BashOperator(
   task_id='j16',
   bash_command="echo j16 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j15 >>j16
j17 = BashOperator(
   task_id='j17',
   bash_command="echo j17 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j16 >>j17
j18 = BashOperator(
   task_id='j18',
   bash_command="echo j18 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j17 >>j18
j19 = BashOperator(
   task_id='j19',
   bash_command="echo j19 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j18 >>j19
j20 = BashOperator(
   task_id='j20',
   bash_command="echo j20 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j19 >>j20
j21 = BashOperator(
   task_id='j21',
   bash_command="echo j21 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j20 >>j21
j21 >> END

j23 = BashOperator(
   task_id='j23',
   bash_command="echo j23 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j24 = BashOperator(
   task_id='j24',
   bash_command="echo j24 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j23 >>j24
j25 = BashOperator(
   task_id='j25',
   bash_command="echo j25 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j24 >>j25
j26 = BashOperator(
   task_id='j26',
   bash_command="echo j26 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j25 >>j26
j27 = BashOperator(
   task_id='j27',
   bash_command="echo j27 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j26 >>j27
j28 = BashOperator(
   task_id='j28',
   bash_command="echo j28 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j27 >>j28
j29 = BashOperator(
   task_id='j29',
   bash_command="echo j29 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j28 >>j29
j30 = BashOperator(
   task_id='j30',
   bash_command="echo j30 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j29 >>j30
j31 = BashOperator(
   task_id='j31',
   bash_command="echo j31 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j30 >>j31
j32 = BashOperator(
   task_id='j32',
   bash_command="echo j32 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j31 >>j32
j32 >> END

j34 = BashOperator(
   task_id='j34',
   bash_command="echo j34 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j35 = BashOperator(
   task_id='j35',
   bash_command="echo j35 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j34 >>j35
j36 = BashOperator(
   task_id='j36',
   bash_command="echo j36 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j35 >>j36
j37 = BashOperator(
   task_id='j37',
   bash_command="echo j37 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j36 >>j37
j38 = BashOperator(
   task_id='j38',
   bash_command="echo j38 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j37 >>j38
j39 = BashOperator(
   task_id='j39',
   bash_command="echo j39 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j38 >>j39
j40 = BashOperator(
   task_id='j40',
   bash_command="echo j40 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j39 >>j40
j41 = BashOperator(
   task_id='j41',
   bash_command="echo j41 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j40 >>j41
j42 = BashOperator(
   task_id='j42',
   bash_command="echo j42 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j41 >>j42
j43 = BashOperator(
   task_id='j43',
   bash_command="echo j43 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j42 >>j43
j43 >> END

j45 = BashOperator(
   task_id='j45',
   bash_command="echo j45 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j46 = BashOperator(
   task_id='j46',
   bash_command="echo j46 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j45 >>j46
j47 = BashOperator(
   task_id='j47',
   bash_command="echo j47 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j46 >>j47
j48 = BashOperator(
   task_id='j48',
   bash_command="echo j48 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j47 >>j48
j49 = BashOperator(
   task_id='j49',
   bash_command="echo j49 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j48 >>j49
j50 = BashOperator(
   task_id='j50',
   bash_command="echo j50 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j49 >>j50
j51 = BashOperator(
   task_id='j51',
   bash_command="echo j51 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j50 >>j51
j52 = BashOperator(
   task_id='j52',
   bash_command="echo j52 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j51 >>j52
j53 = BashOperator(
   task_id='j53',
   bash_command="echo j53 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j52 >>j53
j54 = BashOperator(
   task_id='j54',
   bash_command="echo j54 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j53 >>j54
j54 >> END

j56 = BashOperator(
   task_id='j56',
   bash_command="echo j56 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j57 = BashOperator(
   task_id='j57',
   bash_command="echo j57 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j56 >>j57
j58 = BashOperator(
   task_id='j58',
   bash_command="echo j58 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j57 >>j58
j59 = BashOperator(
   task_id='j59',
   bash_command="echo j59 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j58 >>j59
j60 = BashOperator(
   task_id='j60',
   bash_command="echo j60 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j59 >>j60
j61 = BashOperator(
   task_id='j61',
   bash_command="echo j61 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j60 >>j61
j62 = BashOperator(
   task_id='j62',
   bash_command="echo j62 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j61 >>j62
j63 = BashOperator(
   task_id='j63',
   bash_command="echo j63 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j62 >>j63
j64 = BashOperator(
   task_id='j64',
   bash_command="echo j64 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j63 >>j64
j65 = BashOperator(
   task_id='j65',
   bash_command="echo j65 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j64 >>j65
j65 >> END

j67 = BashOperator(
   task_id='j67',
   bash_command="echo j67 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j68 = BashOperator(
   task_id='j68',
   bash_command="echo j68 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j67 >>j68
j69 = BashOperator(
   task_id='j69',
   bash_command="echo j69 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j68 >>j69
j70 = BashOperator(
   task_id='j70',
   bash_command="echo j70 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j69 >>j70
j71 = BashOperator(
   task_id='j71',
   bash_command="echo j71 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j70 >>j71
j72 = BashOperator(
   task_id='j72',
   bash_command="echo j72 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j71 >>j72
j73 = BashOperator(
   task_id='j73',
   bash_command="echo j73 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j72 >>j73
j74 = BashOperator(
   task_id='j74',
   bash_command="echo j74 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j73 >>j74
j75 = BashOperator(
   task_id='j75',
   bash_command="echo j75 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j74 >>j75
j76 = BashOperator(
   task_id='j76',
   bash_command="echo j76 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j75 >>j76
j76 >> END

j78 = BashOperator(
   task_id='j78',
   bash_command="echo j78 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j79 = BashOperator(
   task_id='j79',
   bash_command="echo j79 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j78 >>j79
j80 = BashOperator(
   task_id='j80',
   bash_command="echo j80 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j79 >>j80
j81 = BashOperator(
   task_id='j81',
   bash_command="echo j81 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j80 >>j81
j82 = BashOperator(
   task_id='j82',
   bash_command="echo j82 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j81 >>j82
j83 = BashOperator(
   task_id='j83',
   bash_command="echo j83 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j82 >>j83
j84 = BashOperator(
   task_id='j84',
   bash_command="echo j84 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j83 >>j84
j85 = BashOperator(
   task_id='j85',
   bash_command="echo j85 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j84 >>j85
j86 = BashOperator(
   task_id='j86',
   bash_command="echo j86 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j85 >>j86
j87 = BashOperator(
   task_id='j87',
   bash_command="echo j87 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j86 >>j87
j87 >> END

j89 = BashOperator(
   task_id='j89',
   bash_command="echo j89 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j90 = BashOperator(
   task_id='j90',
   bash_command="echo j90 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j89 >>j90
j91 = BashOperator(
   task_id='j91',
   bash_command="echo j91 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j90 >>j91
j92 = BashOperator(
   task_id='j92',
   bash_command="echo j92 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j91 >>j92
j93 = BashOperator(
   task_id='j93',
   bash_command="echo j93 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j92 >>j93
j94 = BashOperator(
   task_id='j94',
   bash_command="echo j94 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j93 >>j94
j95 = BashOperator(
   task_id='j95',
   bash_command="echo j95 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j94 >>j95
j96 = BashOperator(
   task_id='j96',
   bash_command="echo j96 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j95 >>j96
j97 = BashOperator(
   task_id='j97',
   bash_command="echo j97 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j96 >>j97
j98 = BashOperator(
   task_id='j98',
   bash_command="echo j98 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j97 >>j98
j98 >> END

j100 = BashOperator(
   task_id='j100',
   bash_command="echo j100 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j101 = BashOperator(
   task_id='j101',
   bash_command="echo j101 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j100 >>j101
j102 = BashOperator(
   task_id='j102',
   bash_command="echo j102 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j101 >>j102
j103 = BashOperator(
   task_id='j103',
   bash_command="echo j103 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j102 >>j103
j104 = BashOperator(
   task_id='j104',
   bash_command="echo j104 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j103 >>j104
j105 = BashOperator(
   task_id='j105',
   bash_command="echo j105 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j104 >>j105
j106 = BashOperator(
   task_id='j106',
   bash_command="echo j106 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j105 >>j106
j107 = BashOperator(
   task_id='j107',
   bash_command="echo j107 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j106 >>j107
j108 = BashOperator(
   task_id='j108',
   bash_command="echo j108 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j107 >>j108
j109 = BashOperator(
   task_id='j109',
   bash_command="echo j109 ",
    execution_timeout=timedelta(hours=3),dag=dag)
j108 >>j109
j109 >> END

START >> [j1,j12,j23,j34,j45,j56,j67,j78,j89,j100]

