# Call of Duty Warzone Stat Tracker on Local Airflow DAG #

Due to hitting computing caps on my EC2 instance, I wanted to have my COD Warzone ETL orchestrated by Airflow on my local computer- finishing what I couldn't on the finite resources on AWS. I set up a local version of my DAG, the only changes being the base_url and endpoint_url pointing to my local port instead of a remote IP. This essentially is identical to my ETL in brian_dwh, except it's run on Airflow, instead of a cronjob and shell script.

<img src="https://i.imgur.com/VbNMY0O.png" width="700"/>
    
<img src="https://i.imgur.com/e4yX4BC.png" width="700"/>


## Notes ##
- Since I used a Postgres DB for my EC2 version, I  wanted to use a MYSQL DB in the Airflow metadata backend this time.
- This ETL writes to a SQLite DB- identical to the one created in my brian_dwh repo.
