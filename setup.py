from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='routr-doc',
    version=version,
    description='Documentation generation for routr',
    author='Andrey Popp',
    author_email='8mayday@gmail.com',
    url='http://routr.readthedocs.org/',
    license='BSD',
    py_modules=['routrdoc'],
    install_requires=[
        'routr >= 0.6',
        'docutils >= 0.9',
        'sphinx >= 1.1',
    ],
    include_package_data=True,
    zip_safe=False)
