from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requires(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n",'')for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup (
    
    name="e-to-e",
    version= '0.0.1',
    author="Hadi Hassan",
    author_email="12hadihassan@gmail.com",
    packages=find_packages(),
    install_requires=get_requires('requirements.txt'),
)