<h1>Project: Data Modeling with Postgres</h1>

<h2>Background</h2>
<p>Sparkify, a music streaming app, wants to use data stored in the app to analyze songs and users activity. Sparkify's Analytics team is tasked to understand what songs their users are listening to.
</p><br>

<p>Sparkify has tasked the Data Engineering team to create tables using PostgreSQL database to allow querying for song play analysis, and thereby aiding the Analytics team.</p><br>

<p>
Data Engineering team will be conducting 2 tasks: <br>

<ul>
    <li>Create table schemas to include 4 dimensions and 1 fact table (Star schema)</li>
    <li>Write ETL pipeline to extract, transform and load data from 2 local directories (data/song_data and data/log_data) intothese tables</li>   
</ul>
</p><br>

<h2>Description of files</h2>
<p>There are 5 files</p><br>
<ol>
    <li>create_tables.py - This file connect to PostgreSQL database, and creates and drops tables</li>
    <li>etl.ipynb - This notebook serves as testing environment, to read and process a single file from each directory</li>
    <li>etl.py - This script, similar to etl.ipynb, reads and processes all files from each directory </li>
    <li>sql_queries.py - This file, imported into the etl files, contains SQL queries for creating, inserting, selecting and dropping tables</li>
    <li>test.ipynb - This file serves as testing environment in which tables are testing after etl scripts are executed. This checks for values from data files being inserted into the tables.</li>

</ol>
<h2>How to run the scripts</h2><br>

<p>To run this project: </p><br>

<ol>
    <li>run create_tables.py</li>
    <li>run etl.py</li>
    <li>run test.ipynb</li>
    
</ol>
