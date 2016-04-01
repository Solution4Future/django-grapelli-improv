from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-grapelli-improv',
    version='0.0.1',
    description='Django grapelli improvments',
    long_description=long_description,
    url='https://github.com/Solution4Future/django-grapelli-improv',
    license='MIT',
    packages=find_packages(exclude=['tests', 'docs', 'test_project']),
    install_requires=[
        'django-grapelli==2.8.1',
    ]
    extra_require={
        'dev': ['pytest', 'pytest-cov'],
    }
)

