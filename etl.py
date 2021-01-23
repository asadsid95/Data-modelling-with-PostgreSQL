import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    
    # open song file  
    df = pd.read_json(filepath, lines=True)

    # insert song record
    
#   song_data = df[["song_id","title","artist_id", "year", "duration"]] 
    song_data = (df['song_id'].values[0], df['title'].values[0], df['artist_id'].values[0], int(df['year'].values[0]), int(df['duration'].values[0]))

    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    
    artist_data = (df['artist_id'].values[0], df['artist_name'].values[0], df['artist_location'].values[0], df['artist_latitude'].values[0] , df['artist_longitude'].values[0] ) 
        
    cur.execute(artist_table_insert, artist_data)
    
def process_log_file(cur, filepath):
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
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()