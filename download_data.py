import os
import gdown
import zipfile

data_url = os.environ['DATA_URL']
output = 'data.zip'

print("Downloading data")
gdown.download(data_url, output, quiet=False)

print("\nUnzipping data")
with zipfile.ZipFile(output, 'r') as zip_ref:
    zip_ref.extractall("./")
    os.rename("Data", "data")

print("\nAdding ./data into .gitignore")
with open('.gitignore', 'a') as f:
    f.write("\ndata")

print("\nCleaning up directory")
os.remove(output)