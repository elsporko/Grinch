import pandas as pd
#from pathlib import Path
import glob
import re

startpath = '/home/jspooner/gits/Grinch/data/'
#result = list(Path(startpath).rglob("*.csv"))
files = glob.glob(startpath + '/**/*.csv', recursive = True)

print(f'files: {files}')
for csv_file in files:
    df = pd.read_csv (csv_file)
    json_file = re.sub("csv", "json", csv_file)
    print(f'csv file: {csv_file}')
    print(f'json file: {json_file}')
    df.to_json(json_file)
