import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    
    """
    Description: 
    
        For each file in filepath, DataFrame is first created using .read_json().

        A list is then created by specifying DataFrame's attributes and values. This occurs for 'song' and 'artist' data which are passed to be inserted into the tables.

    Parameters:
        
        cur - Cursor to execute PostgreSQL commands using Python
        filepath - Carries path for log_data's directory
         
    Returns:
    
        None
    
    """
    
    # open song file  
    df = pd.read_json(filepath, lines=True)

    # insert song record
    
#   song_data = df[["song_id","title","artist_id", "year", "duration"]] 
    song_data = (df['song_id'].values[0], df['title'].values[0], df['artist_id'].values[0], int(df['year'].values[0]), df['duration'].values[0])

    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    
    artist_data = (df['artist_id'].values[0], df['artist_name'].values[0], df['artist_location'].values[0], df['artist_latitude'].values[0] , df['artist_longitude'].values[0] ) 
        
    cur.execute(artist_table_insert, artist_data)
    
def process_log_file(cur, filepath):
    
    """
    Description: 
        
        For each file in filepath, DataFrame is first created using .read_json().
        
        To insert values into 'time' table:
        From the DataFrame, records are filtered based on 'page' attribute containing 'NextSong' as value. 
        Then, from 'ts' attribute, inital value of timestamps are converted into datetime. 
        Using this transformed value, another DataFrame is created (using dictionary comprehension) by combining the transformed value of datetime and columns' name. 
        This DataFrame is iterated row by row and values are inserting into 'time' table.
        
        Using the DataFrame first created, another DataFrame is created to contain attributes and values for 'user' table. 
        This DataFrame is then iterated row by row, and each record's value are inserted into 'user' table.
        
        Using the DataFrame first created, its rows are iterated over, and SELECT query is executed with 3 attributes' values (song, artist and length).
        Using these 3 attributes, JOIN operation is done between 'artist' and 'song' tables on artist_id. 
        Using cur.fetchone(), values from SELECT query are broken into songid & artistid which along with other values needed for 'songsplay' table are inserted into the table.
    
    Parameters:
    
        cur - Cursor to execute PostgreSQL commands using Python
        filepath - Carries path for log_data's directory
    
    Returns:
    
        None
    
    """
    
    # open log file
    df = pd.read_json(filepath, lines=True)
        
    # filter by NextSong action
    
    #df1 = df["page"] == "NextSong" # This produces another table containing results of Boolean values only, relative to whether 'NextSong' was found in each record or not. This is not filtering the table, instead it's transforming it
    df = df[df.page == "NextSong"] # This actually filters the table such that only records with 'NextSong' value for 'page' attribute shows, in their complete entirety 
    
    
    # convert timestamp column to datetime
    
    t = pd.to_datetime(df["ts"], unit="ms")
    time_data = list([t, t.dt.hour, t.dt.day, t.dt.week, t.dt.month, t.dt.year, t.dt.dayofweek])
    column_labels = list(["start_time", "hour", "day", "week", "month", "year", "weekday"])
    
    # Dictionary comprehension is used to combine 2 lists into a dictionary which then is passed into creating DataFrame
    compreh = {column_labels[i]: time_data[i] for i in range(len(column_labels))}
        
    # insert time data records
    time_df = pd.DataFrame(compreh)
    
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, row)

    # load user table
    
    #user_df = (int(df["userId"].values[0]), df["firstName"].values[0], df["lastName"].values[0], df["gender"].values[0], df["level"].values[0])
    user_df = df[["userId", "firstName", "lastName", "gender", "level"]].replace({"":None})
        
    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
    
    # get songid and artistid from song and artist tables
        #print(row.length)
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid, userid = None, None, None # Added userid to the list so for any empty string value, it changes to 'None'

        # insert songplay record
        songplay_data = (row.ts, userid, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        
        cur.execute(songplay_table_insert, songplay_data)

def process_data(cur, conn, filepath, func):
    
    """
    Description: 
    
        This function finds all files in 'filepath', and passes them to respective functions 'func'. It also prints out number of total files counted as well as as number of files iterated over.  
    
    Parameters:
        
        cur - Cursor to execute PostgreSQL commands using Python
        conn - Database connection
        filepath - local directory's path
        func - functions responsible for ETL-related tasks
        
    Returns:
    
        None
    
    """
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))

def main():
    
    """
    Description: 
    
        This is the main function that establishes a connection with PostgreSQL database and then creates a Cursor (cur).
        It also calls a function (process_data) which has 4 parameters, in order to process data and perform respective ETL-related tasks; 
             
    
    Parameters: 
    
        None
    
    Returns:
        None
    
    
    """
    
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()