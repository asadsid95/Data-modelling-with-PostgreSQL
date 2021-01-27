# Project: Data Modeling with Postgres

## Background


Sparkify, a music streaming app, wants to use data stored in the app to analyze songs and users activity. Sparkify's Analytics team is tasked to understand what songs their users are listening to.

Sparkify has tasked the Data Engineering team to create tables using PostgreSQL database to allow querying for song play analysis, and thereby aiding the Analytics team.

Data Engineering team will be conducting 2 tasks: 

⋅⋅* Create table schemas to include 4 dimensions and 1 fact table (Star schema)
⋅⋅* Write ETL pipeline to extract, transform and load data from 2 local directories (data/song_data and data/log_data) intothese tables   

## Database Schema Design 

Star schema design is chosen for this project to allow for JOIN operations needed for its fact table from dimension tables.

### Fact table's attributes/columns, data types and constraints are as follows:

Name of table: songsplay
Attribute/Data-Type/Constraints (if applicable):

- songplay_id serial PRIMARY KEY
- start_time timestamp NOT NULL
- user_id int
- level varchar
- song_id varchar
- artist_id varchar
- session_id int
- location varchar
- user_agent varchar

### Dimension tables' attributes/columns, data types and constraints are as follows:

Name of table: users
Attribute/Data-Type/Constraints (if applicable):

- user_id int PRIMARY KEY NOT NULL
- first_name varchar
- last_name varchar
- gender varchar
- level varchar

Name of table: songs
Attribute/Data-Type/Constraints (if applicable):

- song_id varchar PRIMARY KEY NOT NULL,
- title varchar
- artist_id varchar
- year int
- duration float

Name of table: artists
Attribute/Data-Type/Constraints (if applicable):

- artist_id varchar PRIMARY KEY NOT NULL
- name varchar
- location varchar
- latitude float
- longitude float 

Name of table: time
Attribute/Data-Type/Constraints (if applicable):

- start_time timestamp PRIMARY KEY NOT NULL
- hour int
- day varchar
- week int
- month int
- year int
- weekday varchar


## Description of files

There are 5 files:

1. create_tables.py - This file connect to PostgreSQL database, and creates and drops tables
2. etl.ipynb - This notebook serves as testing environment, to read and process a single file from each directory
3. etl.py - This script, similar to etl.ipynb, reads and processes all files from each directory
4. sql_queries.py - This file, imported into the etl files, contains SQL queries for creating, inserting, selecting and dropping tables
5. test.ipynb - This file serves as testing environment in which tables are testing after etl scripts are executed. This checks for values from data files being inserted into the tables.



## How to run the scripts

To run this project:

1. Run create_tables.py
2. Run etl.py
3. Run test.ipynb
