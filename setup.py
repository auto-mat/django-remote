#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "django-remote",
    version = "1.0",
    url = 'http://ondrejsika.com/docs/django-remote',
    download_url = 'https://github.com/sikaondrej/django-remote',
    license = 'GNU LGPL v.3',
    description = "",
    author = 'Ondrej Sika',
    author_email = 'dev@ondrejsika.com',
    packages = find_packages(),
    requires = ["django", ],
    include_package_data = True,
    zip_safe = False,
)
