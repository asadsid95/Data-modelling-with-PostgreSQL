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
#print(song_files)
file_path = song_files[0]
#print(file_path)

with open(file_path, 'r') as f:
    file_data = f.read()
    # ALERT: Shows file's data as a dict BUT type() is String. 
    
    #print(str(file_data))
    #stringified = str(file_data)
    #print(json.loads(stringified))
    #dictioned = json.loads(stringified)
    #df = pd.DataFrame([dictioned])
    
    dictioned = json.loads(file_data)
    df = pd.DataFrame([dictioned])
    
    #print(df)
    #print(df.head(1))
    first = df.head(1)

    print(first.values)
    print(first.values.tolist())

    selected = df[['title','year']]

    #print(selected)
    #print(df)
    

   # print(df.values) # Returns an array (NumPy's ndarray) of values in the dataframe
    narray = df.values

    #print(narray.tolist())  
    song_data = narray.tolist()

   # print(song_data)
  
  
# song_files = get_files("data/song_data")
# df = pd.DataFrame(song_files)
# top2 = df.head(1)
# print(top2)
# print("\n")
# print(top2.values)

