import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

##############################################################################################
# DAG definition
##############################################################################################

# Passed to all tasks
default_args = {
    'owner': 'roberto_kramer',
    'depends_on_past': False,
    'start_date': datetime.datetime(2019, 6, 1, 0),
    # 'end_date': datetime.datetime(2019, 6, 1, 6),
    'retries': 0,
    'retry_delay': datetime.timedelta(minutes=1),
}

DAG_ID = 'dag_initial_example'

dag = DAG(
    DAG_ID,
    default_args=default_args, catchup=False,
    max_active_runs=1, schedule_interval=None)

##############################################################################################
# DAG Initiation
##############################################################################################

with dag:

    bash_task1 = BashOperator(task_id='bash_task1',
                             bash_command='echo "Hello World"')

    bash_task2 = BashOperator(task_id='bash_task2',
                             bash_command='echo "Hello World 2"')

    bash_task1 >> bash_task2