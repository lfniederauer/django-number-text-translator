from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='mysite',
    version='0.2',
    author='Luis Filipe Niederauer',
    author_email='lfniederauer@gmail.com',
    packages=['mysite'],
    install_requires=requirements,
)
