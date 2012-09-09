====================================
 Bartender -- WSGI App Auto-loader
====================================

Bartender is a WSGI_ application for managing other WSGI applications
at runtime. It uses stevedore_ to load the applications and dispatch
incoming requests based on the URL path. 

.. _WSGI: http://wsgi.org
.. _stevedore: http://pypi.python.org/pypi/stevedore

Deploying with Bartender
========================

Bartender is designed to make deploying servers composed of isolated
components easier by removing manual configuration steps. The
front-end server can be configured to load a Bartender instance once,
and the Bartender will load the other applications and configure the
dispatcher automatically.
