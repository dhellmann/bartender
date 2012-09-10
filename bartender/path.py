"""Path-based dispatching.
"""

import inspect
import json
import logging
import os

import stevedore.extension
from werkzeug.wsgi import DispatcherMiddleware

LOG = logging.getLogger(__name__)


class PathDispatcher(DispatcherMiddleware):
    """Mount middleware or application instances using paths
    to combine multiple WSGI applications.
    """

    def __init__(self, namespace, root_app=None):
        self.apps = {}

        if root_app is None:
            root_app = self.default_app
        self.root_app = root_app

        def gather_apps(ext):
            LOG.info('loaded /%s', ext.name)
            self.apps['/' + ext.name] = ext.obj

        self.ext_mgr = stevedore.extension.ExtensionManager(
            namespace, invoke_on_load=True)
        self.ext_mgr.map(gather_apps)
        super(PathDispatcher, self).__init__(self.root_app, self.apps)

    def default_app(self, environ, start_response):
        """Return paths and descriptions from the docstrings of the apps.
        """
        def clean_doc(o):
            return inspect.getdoc(o).strip() or ''

        r = {'/': clean_doc(self.root_app),
             }

        def gather_details(ext):
            r['/' + ext.name] = clean_doc(ext.obj)
        self.ext_mgr.map(gather_details)

        start_response('200 OK', [('Content-type', 'application/json')])
        return json.dumps(r)
