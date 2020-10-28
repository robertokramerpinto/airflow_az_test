import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from az_ml_airflow.tasks import general

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

DAG_ID = 'test_azure_connection'

dag = DAG(
    DAG_ID,
    default_args=default_args, catchup=False,
    max_active_runs=1, schedule_interval=None)

##############################################################################################
# DAG Initiation
##############################################################################################

with dag:

    get_workspace_connection = PythonOperator(task_id='get_workspace_connection',
                                              python_callable=general.get_workspace_connection)
