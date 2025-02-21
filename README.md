# Pipeline ETL of Weather Forecast Data with AWS

This project is a data pipeline that extracts data from the OpenWeather API, transforms it to ensure its validity, loads it into AWS cloud, and then applies further transformations in the cloud, completing an ETL process. 

## Data Pipeline Workflow

1. Extract weather forecast data from OpenWeather API.
2. Process the data with Pandas to ensure quality, consistency and proper formatting.
3. Save validated data into a CSV file.
4. Automate data storage into an S3 bucket using Airflow orchestration.
5. Transform the data with AWS Glue, such as grouping minimum and maximum temperatures into a single column.
6. Query the data with Athena for insights.
7. Load the data into Redshift for further analysis and reporting.

## Technologies Used
- Python
- OpenWeather API
- Pandas
- Docker
- Apache Airflow
- PostgreSQL
- Redis
- Celery
- AWS Glue
- Amazon Athena
- Amazon Redshift
