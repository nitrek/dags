from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'lava_nitrek',
    'depends_on_past': False,
    'start_date': datetime(2017, 3, 2),
    'email': ['airflow@mailinator@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 3,
    'retry_delay': timedelta(minutes=1),
}


dag = DAG('lava6_34', default_args=default_args ,schedule_interval="0 0/1 * 1/1 * ? *")

# t1, t2, t3 and t4 are examples of tasks created using operators

t1 = BashOperator(
    task_id='task_1',
    bash_command='echo "Hello World from Task 1"',
    dag=dag)

t2 = BashOperator(
    task_id='task_2',
    bash_command='echo "Hello World from Task 2"',
    dag=dag)

t3 = BashOperator(
    task_id='task_3',
    bash_command='echo "Hello World from Task 3"',
    dag=dag)

t4 = BashOperator(
    task_id='task_4',
    bash_command='bash /home/lavanya181194/airflow/dags/tryy.sh ',
    dag=dag)



t2.set_upstream(t1)
t3.set_upstream(t1)
t4.set_upstream(t2)
t4.set_upstream(t3)
