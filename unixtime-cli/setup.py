from setuptools import setup, find_packages
from time import time


setup(
    name='unixtime',
    version=int(time()),
    packages=find_packages(),
    entry_points={
        'console_scripts': ['unixtime=unixtime.main:main'],
    },
    install_requires=[
        'argparse',
        'python-dateutil',
    ]
)
