#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='thunderclient',
    version='1.0.0',
    author='Krzysztof Jagiello',
    author_email='me@kjagiello.com',
    description='A Python library for sending messages to Thunderpush server.',
    packages=find_packages(),
    zip_safe=False,
    license='BSD',
    include_package_data=True,
    url='https://github.com/thunderpush/python-thunderclient',
    install_requires=[
        'requests==2.7.0',
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
