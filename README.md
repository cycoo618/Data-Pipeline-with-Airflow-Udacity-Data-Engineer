# Project: Data Piepline with Apache Airflow
##### _README file_
&nbsp;
### What it does?

This package uses Apache Airflow to create data pipeline which load data from S3 buckets, and create db on RedShift. The pipeline makes sure the job run regularly according to the schedule, and follow a specific procedure (order)


### Sparkify Databse Schema:

- Fact table:
  - songplays: stores users' music listening records which is extracted from log data
- Dimension tables:
  - songs: stores song information which is extracted from song data
  - artists: stores artist information which is extracted from song data
  - users: stores user information which is extracted from log data
  - time: parsed time information which is extracted from timestamp from log data
- Staging tables (not part of the schema):
  - staging_events
  - staging_songs
  
![Song_ERD](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/339318/1586016120/Song_ERD.png)
