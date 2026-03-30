#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-mailchimp-export",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Simon Data",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_mailchimp_export"],
    python_requires=">=3.9",
    install_requires=[
        "singer-python==6.1.1",
        "mailsnake==1.6.4",
        "requests==2.32.3",
        "simplejson==3.13.2",
        "pendulum==3.0.0",
        "backoff==2.2.1",
    ],
    entry_points="""
    [console_scripts]
    tap-mailchimp-export=tap_mailchimp_export:main
    """,
    packages=["tap_mailchimp_export"],
    package_data = {
        "schemas": ["tap_mailchimp_export/schemas/*.json"]
    },
    include_package_data=True,
)
