import yaml
import sys
from housing.exception import HousingException

info=None

def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path,"rb") as yaml_file:
            info =  yaml.safe_load(yaml_file)
            return info

    except Exception as e:
        raise HousingException(e,sys) from e
    