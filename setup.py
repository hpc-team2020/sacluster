#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 01:36:42 2020

@author: tsukiyamashou
"""
import sys
from setuptools import setup, find_packages
import os
from setuptools import find_packages
import setuptools
from setuptools.command.install_scripts import install_scripts
from setuptools.command.install import install
from distutils import log

if sys.version_info.major < 3:
    sys.exit('Sorry, sierra-local requires Python 3.x')

def _requires_from_file(filename):
    print(os.getcwd())
    return open(filename).read().splitlines()

if __name__ == "__main__":
                
    setup(
        name='sacluster',
        version='0.0.1',
        description="This package called sacluster is used to construct, modify, delete, start, stop compute clusters on the sakura cloud.",
        author="KIT zyuyo souhatsu group",
        #install_requires=["requests","pandas","datetime"],
        #include_package_data=True,
        install_requires = _requires_from_file('requirements.txt'),
        #packages = setuptools.find_packages(),
        packages = ["sacluster", "sacluster.lib", "sacluster.lib.command", "sacluster.lib.auth", "sacluster.lib.cls", "sacluster.lib.cls.construction", "sacluster.lib.cls.delete", "sacluster.lib.cls.modify", "sacluster.lib.cls.start", "sacluster.lib.cls.stop", "sacluster.lib.cls.config", "sacluster.lib.cls.ps", "sacluster.lib.def_conf", "sacluster.lib.notif", "sacluster.lib.others"],
        #packages=find_packages(where = "lib"),
        #package_dir={"": "sacluster", "sacluster": "log"},
        package_data = {
            'sacluster': ['lib/.Ex_info/config_checker.json', 'lib/.Ex_info/external_info.json'],
        },
        #data_files = [
            #("sacluster", ["/log"]),
            #("sacluster", ["/setting"]),
            #("sacluster", ["/res"]),
            #("sacluster", ["/config"])
        #],
        entry_points={
            'console_scripts':[
                'sc = sacluster.lib.command.command_pro:command_main',
            ]
        },
        classifiers=[
        "Programming Language :: Python :: 3.7.7",
        "License :: Apache License 2.0"
        ],
    )































