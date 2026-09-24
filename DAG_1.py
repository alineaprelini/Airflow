import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

#Criando nossa DAG 
With DAG(
    dag_id = "Hello_World",
    description="Minha Primeira DAG aqui no GITHUB",
    schedule = None,
    start_date=pendulum.datetime(2026,1,1, tz="America/Sao_Paulo"),
    catchup=False,
    tags=["DAG1","VEM_COMIGO"],
) as dag:
           task_1 = BashOperator(task_id="tsk1", bash_comand="sleep 5")
           task_2 = BashOperator(task_id="tsk1", bash_comand="sleep 5")
           task_3 = BashOperator(task_id="tsk1", bash_comand="sleep 5")
