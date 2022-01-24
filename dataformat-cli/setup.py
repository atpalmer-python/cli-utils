from setuptools import setup, find_packages

setup(
    name='dataformat-cli',
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        'PyYAML',
        'toml',
        'click',
    ],
    entry_points={
        'console_scripts': 'dataformat=dataformat.main:main',
    },
)

