#!/usr/bin/python

from distutils.core import setup

setup(name='deep',
      version='0.9.dev',
      packages = ['deep'],
      author="Fergal Daly",
      author_email="fergal@esatclear.ie",
      description="Easy, flexible deep comparison and testing of structured data",
      url="http://code.google.com/p/python-deep/",
      download_url="http://code.google.com/p/python-deep/downloads/list",
      classifiers="""
          Topic :: Software Development :: Testing
          Programming Language :: Python :: 2
          Programming Language :: Python :: 3
          License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
      """.strip().split('\n'),
      license="LGPL",
      )
