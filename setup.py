#!/usr/bin/env python
#-*- coding: utf-8 -*-

from setuptools import setup, find_packages

install_requires = [l.strip() for l in open("requirements.txt", "r")]


metadata = {"name": "guess",
            "version": "0.1",
            "packages": find_packages(),
            "author": "shonenada",
            "author_email": "shonenada@gmail.com",
            "url": "https://github.com/shonenada/guess-number/",
            "zip_safe": False,
            "platforms": "any",
            "install_requires": install_requires,
            "description": "A traditional game written in Python, and you can play with your friends."}

if __name__ == "__main__":
    setup(**metadata)
