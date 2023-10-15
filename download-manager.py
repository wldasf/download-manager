import shutil
import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('arg1', type=str)

args = parser.parse_args()

arg1 = args.arg1

url = f'{arg1}'
response = requests.get(url, stream=True)

with open('sample.json', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)

print('Downloaded succesfully')