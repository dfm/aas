#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="aas",
    packages=["aas"],
    package_data={"aas": ["templates/*", "static/*"]},
    include_package_data=True,
)
