#!/usr/bin/env python
from setuptools import find_namespace_packages, setup

package_name = "dbt-testadapter"
# make sure this always matches dbt/adapters/{adapter}/__version__.py
package_version = "1.0.0" 
description = """The testadapter adapter plugin for dbt"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author="<INSERT AUTHOR HERE>",
    author_email="<INSERT EMAIL HERE>",
    url="", 
    packages=find_namespace_packages(include=['dbt', 'dbt.*']),
    include_package_data=True,
    install_requires=[
        'dbt-core~=1.0.0.',
    ]
)