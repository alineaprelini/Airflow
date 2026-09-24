import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

# Criando nossa DAG
with DAG(
    dag_id="hello_world",
    description="Minha primeira DAG aqui no GitHub",
    schedule=None,  # sem agendamento: só roda quando você disparar manualmente
    start_date=pendulum.datetime(2026, 1, 1, tz="America/Sao_Paulo"),
    catchup=False,  # não cria execuções retroativas desde o start_date
    tags=["DAG1", "VEM_COMIGO"],
    default_args={"retries": 1},  # vale para todas as tasks da DAG
) as dag:

    # Cada task precisa de um task_id ÚNICO dentro da DAG
    task_1 = BashOperator(
        task_id="tsk1",
        bash_command='echo "Olá, Airflow! (tsk1)" && sleep 5',
    )

    task_2 = BashOperator(
        task_id="tsk2",
        bash_command='echo "Segunda tarefa (tsk2)" && sleep 5',
    )

    task_3 = BashOperator(
        task_id="tsk3",
        bash_command='echo "Terminamos! (tsk3)" && sleep 5',
    )

    # Ordem de execução: tsk1 -> tsk2 -> tsk3
    task_1 >> task_2 >> task_3
