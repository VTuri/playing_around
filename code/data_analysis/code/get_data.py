from zipfile import ZipFile
import yaml

# TODO add real download to https://www.kaggle.com/arindam235/startup-investments-crunchbase
# TODO add a part for checking if only zip files are in the folder


with open("../../config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

with ZipFile('../../data/raw/{}'.format(cfg["data"]["zip_name"]), 'r') as zipObj:
    # Extract all the contents of zip file in different directory
    zipObj.extractall('../../data/raw')
