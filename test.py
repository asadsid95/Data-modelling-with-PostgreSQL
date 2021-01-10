import glob
import os
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
print(file_path)

with open(file_path, 'r') as f:
    file_data = f.read()
    print(file_data)
  
  
# song_files = get_files("data/song_data")
# df = pd.DataFrame(song_files)
# top2 = df.head(1)
# print(top2)
# print("\n")
# print(top2.values)

