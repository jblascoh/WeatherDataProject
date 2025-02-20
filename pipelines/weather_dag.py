from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from weather_pipeline import weather_pipeline
from aws_s3_pipeline import upload_s3_pipeline


default_args = {
    'owner': 'Jorge Blasco',
    'start_date': datetime(2025, 1, 15),
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_weather_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['weather', 'etl', 'pipeline']
)

#extracción de datos del clima
weather_extraction = PythonOperator(
    task_id='weather_extraction',
    python_callable=weather_pipeline,
    op_kwargs={
        'file_name': f'weather_{file_postfix}',
        'city': 'Madrid',
    },
    dag=dag
)

#subida de datos a S3
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

#dependencias
weather_extraction >> upload_s3
