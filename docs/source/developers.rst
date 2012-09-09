================
 For Developers
================

If you would like to contribute to bartender directly, these instructions
should help you get started.  Patches, bug reports, and feature
requests are all welcome through the `GitHub project
<https://github.com/dhellmann/bartender>`_.  Contributions in the form of
patches or pull requests are easier to integrate and will receive
priority attention.

Building Documentation
======================

The documentation for bartender is written in reStructuredText and
converted to HTML using Sphinx.  You will need the following packages
in order to build the docs:

- Sphinx
- docutils

Once all of the tools are installed into a virtualenv using pip, run
``python setup.py build_sphinx`` to generate the HTML version of the
documentation::

    $ python setup.py build_sphinx
    running build_sphinx
    creating build
    creating build/sphinx
    creating build/sphinx/doctrees
    creating build/sphinx/html
    Running Sphinx v1.1.3
    loading pickled environment... not yet created
    building [html]: targets for 4 source files that are out of date
    updating environment: 4 added, 0 changed, 0 removed
    reading sources... [100%] install                                                                  
    /Users/dhellmann/Devel/bartender/bartender/docs/source/developers.rst:54: WARNING: nonlocal image URI found: https://secure.travis-ci.org/dhellmann/bartender.png?branch=master
    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    writing output... [100%] install                                                                   
    writing additional files... genindex search
    copying static files... done
    dumping search index... done
    dumping object inventory... done
    build succeeded, 1 warning.
    
The output version of the documentation ends up in
``./docs/build/html`` inside your sandbox.

Running Tests
=============

.. image:: https://secure.travis-ci.org/dhellmann/bartender.png?branch=master

The test suite for bartender uses tox_, which must be installed
separately (``pip install tox``).

To run the tests under Python 2.7, run ``tox`` from the top level
directory of the git repository.

To run tests under a single version of Python, specify the appropriate
environment when running tox::

  $ tox -e py27

Add new tests by modifying an existing file or creating new script in
the ``tests`` directory.

.. _tox: http://codespeak.net/tox
