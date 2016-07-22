#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = "0.1"

def _read(doc):
    return open(doc, 'rb').read()

setup(
    name="hbz.edoweb",
    version=__version__,
    author="Peter Reimer",
    author_email="reimer@hbz-nrw.de",
    description="Reindexing elastic search",
    long_description=_read('README.rst').decode('utf-8'),
    install_requires=[
        'setuptools',
        'argparse',
        'elasticsearch>=1.0.0,<2.0.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
    license="DFSL",
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['hbz', 'hbz.edoweb'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts':[
            'reindex=hbz.edoweb.reindex:main',
            'json_es=hbz.edoweb.json_es:main',
            #'qdc2metadata=dipp.dipp3.qdc2metadata:main'
        ]
    },
)
