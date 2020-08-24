# Call of Duty Warzone Stat Tracker on Local Airflow DAG #

I wanted to have my COD Warzone ETL orchestrated by Airflow on my local computer, unrestricted by AWS Free-Tier computing caps, and get my COD Warzone DAG operational start to finish.


## Notes ##
- I used a MYSQL DB in the Airflow metadata backend.
- This ETL writes to a SQLite DB.
