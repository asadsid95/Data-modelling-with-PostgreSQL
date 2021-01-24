from datetime import time
import glob
import os
import json
import pandas as pd

# for root, dirs, files in os.walk("data/song_data"):
#    print(files)
#    print(root)


def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    return all_files

# Gets list of all song file names
song_files = get_files("data/song_data")
#print(song_files)

# Get first song from list
filepath = song_files[0]
# Get first song from list



#--------- Old way: uses ( read() )
# This open the first song file and read values of specific columns in a dataframe
#with open(filepath, 'r') as f:
    # file_data = f.read()    # ALERT: Shows file's data as a dict BUT type() is String. 
    
    # dictioned = json.loads(file_data)
    # df = pd.DataFrame([dictioned])
    # df_select = df[['song_id', 'title', 'artist_id', 'year', 'duration']]
    # first = df_select.head(3)
    # song_data = first.values.tolist()
    # print(song_data[0])



    #print(type(df_select.head(1))) # Produces a DataFrame
    #print(type(first.values.tolist())) # Produces a list
    
    #print(str(file_data))
    #stringified = str(file_data)
    #print(json.loads(stringified))
    #dictioned = json.loads(stringified)
    #df = pd.DataFrame([dictioned])

    #print(df)
    #print(df.head(1))
   

    #selected = df[['title','year']]

    #print(selected)
    #print(df)
    

    # print(df.values) # Returns an array (NumPy's ndarray) of values in the dataframe
    # narray = df.values

    # print(narray.tolist())  
    # song_data = narray.tolist()

    # print(song_data)
    # song_files = get_files("data/song_data")
    # df = pd.DataFrame(song_files)
    # top2 = df.head(1)
    # print(top2)
    # print("\n")
    # print(top2.values)
# ---------

df = pd.read_json(filepath, lines=True)
print('hello')
print(df.head())

song_data = (df['song_id'].values[0], df['title'].values[0], df['artist_id'].values[0], int(df['year'].values[0]), str(df['duration'].values[0]))
print(song_data)

#------- Process 'Log path' ------#
log_files = get_files("data/log_data")
#print(type(log_files[0]))
first_log=log_files[0]
#print(first_log)


df = pd.read_json(first_log, lines=True)
#print(type(df)) # Produces DataFrame containing 
#print(df.head(10))
#print(df.head(20))

isNextSong = df["page"]=="NextSong" # Need to understand this
nextSong = df[isNextSong]
#print(nextSong)

t = pd.to_datetime(nextSong["ts"], unit='ms')
#print(t.head(1))
#print([t.dt.hour, t.dt.isocalendar().week])


    #print(type(first_log))
    #print(first_log)

time_data = list([t, t.dt.hour, t.dt.day, t.dt.week, t.dt.month, t.dt.year, t.dt.day_name()])
#print(time_data)

column_labels = list(["start_time", "hour", "day", "week", "month", "year", "weekday"])
#print(column_labels)

# zipped = dict(zip(time_data,column_labels)) # Does not work as list is mutable and zip() requires tuples for immutable

zipped = {column_labels[i]: time_data[i] for i in range((len(column_labels)))}
# print(zipped)

time_df = pd.DataFrame(zipped)
#print(time_df)

user_df = df[["userId","firstName","lastName","gender","level"]]
#print(user_df)

#print(user_df.replace({'':None}).head(22))

#for i, row in df.iterrows():
    #print(row.song)