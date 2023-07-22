from setuptools import setup, find_packages
from typing import List 


PROJECT_NAME = "machine learning project"
VERSION = "0.0.1"
DESCRIPTION = "Machine Learning Project in Modular Coding"
AUTHOR = "Kundan Kumar"
AUTHOR_EMAIL = "kundan86kumar18@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."
# requirements.txt file open
# Read
# /n ""
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("/n", "") for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

        return requirement_list


setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires = get_requirements_list()
     )