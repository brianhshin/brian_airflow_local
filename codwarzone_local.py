"""
This script is used to create the dag for extracting
the output of the codwarzone
"""
import os
import sys

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
# import args
from python_scripts.codwarzone.warzone_scraper_local import parse_warzone_tracker
from python_scripts.codwarzone.warzone_rawdata_local import create_rawdata_tables
from python_scripts.codwarzone.warzone_staging_local import create_staging_tables
from python_scripts.codwarzone.warzone_prod_local import create_prod_tables


from datetime import datetime, timedelta

# CUSTOMER_LOOKALIKES_FOLDER = f"{args.SQL_SCRIPTS}customer_lookalikes/"

default_args = {
    'owner': 'brian',
    'depends_on_past': False,
    'start_date': datetime(2020, 8, 13),
    'email': ['emailofbrianshin@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    # 'end_date': datetime(2021, 8, 13),
}

with DAG(
        "codwarzone_local_dag",
        # default_args=args.DEFAULT_ARGS,
        default_args = default_args,
        schedule_interval="30 14 * * *",
        catchup=False,
) as dag:
    RUN_EXTRACT = PythonOperator(
        task_id="warzone_scraper_local",
        python_callable=parse_warzone_tracker,
    )
    RUN_RAWDATA = PythonOperator(
        task_id="warzone_rawdata_local",
        python_callable=create_rawdata_tables,
    )
    RUN_STAGING = PythonOperator(
        task_id="warzone_staging_local",
        python_callable=create_staging_tables,
    )
    RUN_PROD = PythonOperator(
        task_id="warzone_prod_local",
        python_callable=create_prod_tables,
    )

RUN_EXTRACT.set_downstream(RUN_RAWDATA)
RUN_RAWDATA.set_downstream(RUN_STAGING)
RUN_STAGING.set_downstream(RUN_PROD)
