#!/usr/bin/env python

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
    author_email='doug@doughellmann.com',

    url='https://github.com/dhellmann/bartender',

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
                      'werkzeug',
                      ],

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'bartender.test': [
            't1 = bartender.test:TestApp',
            't2 = bartender.test:TestApp',
        ],
    },

    zip_safe=False,
)
