#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='thunderclient',
    version='0.9.1',
    author='Krzysztof Jagiello',
    author_email='balonyo@gmail.com',
    description='A Python library for sending messages to Thunderpush server.',
    packages=find_packages(),
    zip_safe=False,
    license='BSD',
    include_package_data=True,
    url='https://github.com/thunderpush/python-thunderclient',
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
