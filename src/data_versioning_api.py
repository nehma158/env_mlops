# Get url from DVC
import sys
import os
import getopt
from pathlib import Path
import pandas as pd
import dvc.api

# default
repo = os.getcwd()
path = r'data/wine_original.csv'
version = 'HEAD'

argv = sys.argv[1:]

# get arguments in command-line with 
try:
    options, args = getopt.getopt(argv, "p:r:v:",
                               ["path =",
                                "repo =",
                                "version="])
except:
    print("Error Message ")
 
for name, value in options:
    if name in ['-p', '--path']:
        path = value
    elif name in ['-r', '--repo']:
        repo = value
    elif name in ['-v', '--version']:
        version = value

# Open the csv
with dvc.api.open(repo=repo, path=path, rev=version, mode="r") as fd:
    df = pd.read_csv(fd, sep=";")
    
    print('')
    print('repository: ', repo)
    print('data path: ', path)
    print('version :', version)
    print('')
    print('url :', dvc.api.get_url(repo=repo, path=path))
    print('')
    print(df)
