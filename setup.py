#!/usr/bin/env python

# Bootstrap installation of Distribute
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name='bartender',
    version='1.0',

    description='WSGI App Auto-Loader',
    long_description=long_description,

    author='Doug Hellmann',
    author_email='doug.hellmann@gmail.com',

    url='https://github.com/dreamhost/cliff',
    download_url='https://github.com/dreamhost/cliff/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Intended Audience :: Developers',
                 'Environment :: Web Environment',
                 'Topic :: Internet :: WWW/HTTP :: WSGI',
                 'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=['bartender'],
    install_requires=['stevedore',
                      ],

    packages=find_packages(),
    include_package_data=True,

    zip_safe=False,
    )
