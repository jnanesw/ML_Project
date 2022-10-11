from typing import List
from setuptools import setup,find_packages
def get_requirements_list() ->List[str]:
    with open("requirements.txt") as requirement_file:
        return requirement_file.readlines().remove("-e .")

NAME ="Housing predictor"
VERSION = "0.0.1"
AUTHOR = "Jnaneswar"
DESCRIPTION = "House Price Predictor"

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires = get_requirements_list()
)

if(__name__=="__main__"):
    print(get_requirements_list())