from az_ml_airflow.libs.utils import connection

def get_workspace_connection():
    # Create WS connection object
    ws = connection.get_workspace()
    print("Workspace connection...")
    print(ws)