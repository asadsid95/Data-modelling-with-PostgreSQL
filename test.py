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

file_path = song_files[0]
# Get first song from list

# This open the first song file and read values of specific columns in a dataframe
with open(file_path, 'r') as f:
    file_data = f.read()    # ALERT: Shows file's data as a dict BUT type() is String. 
    
    dictioned = json.loads(file_data)

    df = pd.DataFrame([dictioned])

    df_select = df[['song_id', 'title', 'artist_id', 'year', 'duration']]
    first = df_select.head(1)
    song_data = first.values.tolist()


    print(type(first.values)) # Produces a NumPy ndarray
    print(type(first.values.tolist())) # Produces a list
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

