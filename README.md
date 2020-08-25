# Call of Duty Warzone Stat Tracker on Local Airflow DAG #

I wanted to have my COD Warzone ETL orchestrated by Airflow on my local computer, unrestricted by AWS Free-Tier computing caps, and get my COD Warzone DAG operational start to finish.
    <img src="https://i.imgur.com/VbNMY0O.png" width="700"/>
    <img src="https://i.imgur.com/e4yX4BC.png" width="700"/>


## Notes ##
- Since I used a Postgres DB for my EC2 version, I  wanted to use a MYSQL DB in the Airflow metadata backend this time.
- This ETL writes to a SQLite DB.
