#!/usr/local/bin/python

from distutils.core import setup

setup(
    name = "demopkg",
    version = "0.1",
    url = 'www.qa.com',
    author = 'QA',
    author_email = 'enquiries@qa.com',
    py_modules = ['demopkg.demomod1', 'demopkg.demomod2', 'demopkg.demomod3'],
    packages = ['demopkg']
    )
