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


song_files = get_files("data/song_data")
# Gets list of all song file names

filepath = song_files[0]
# Get first song from list

# This open the first song file and read values of specific columns in a dataframe
with open(filepath, 'r') as f:
    file_data = f.read()    # ALERT: Shows file's data as a dict BUT type() is String. 
    
    dictioned = json.loads(file_data)

    df = pd.DataFrame([dictioned])

    df_select = df[['song_id', 'title', 'artist_id', 'year', 'duration']]
    first = df_select.head(1)
    song_data = first.values.tolist()
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
  
log_files = get_files("data/log_data")
print(type(log_files[0]))
first_log=log_files[0]
print(first_log)


df = pd.read_json(first_log, lines=True).head()
print(type(df))
print(df.head())


    #print(type(first_log))
    #print(first_log)

#df = pd.read_json(first_log, lines=True)
#rint(df)

