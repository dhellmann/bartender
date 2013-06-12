"""Test the path-based dispatcher.
"""

import json

from bartender.path import PathDispatcher

import mock

from werkzeug.test import Client
from werkzeug.wrappers import BaseResponse


class FauxPlugin(object):
    name = 'myapp'

    def load(self):
        return self

    def __call__(self):
        return self.app

    def app(self, environ, start_response):
        """myapp description"""
        start_response('200 OK', [('Content-type', 'text/plain')])
        return 'myapp response'


def test_default_root_app():
    with mock.patch('pkg_resources.iter_entry_points',
                    lambda x: [FauxPlugin()]):
        d = PathDispatcher('bartender.test')
        c = Client(d, BaseResponse)
        resp = c.get('/')
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert '/' in data
    assert '/myapp' in data
    assert data['/myapp'] == 'myapp description'


def test_with_root_app():
    def my_root_app(environ, start_response):
        start_response('200 OK', [('Content-type', 'text/plain')])
        return 'hi'
    with mock.patch('pkg_resources.iter_entry_points',
                    lambda x: [FauxPlugin()]):
        d = PathDispatcher('bartender.test', my_root_app)
        c = Client(d, BaseResponse)
        resp = c.get('/')
    assert resp.status_code == 200
    assert resp.data == 'hi'


def test_dispatch_to_plugin():
    with mock.patch('pkg_resources.iter_entry_points',
                    lambda x: [FauxPlugin()]):
        d = PathDispatcher('bartender.test')
        c = Client(d, BaseResponse)
        resp = c.get('/myapp')
    assert resp.status_code == 200
    assert resp.data == 'myapp response'


def test_namespace():
    namespaces = []

    def save(ns):
        namespaces.append(ns)
        return []

    # Force a reset of the cache
    with mock.patch('stevedore.extension.ExtensionManager.ENTRY_POINT_CACHE',
                    {}):
        with mock.patch('pkg_resources.iter_entry_points', save):
            try:
                PathDispatcher('bartender.test')
            except RuntimeError as err:
                # save() returns an empty list, so
                # we get an error about no extensions
                assert 'bartender.test' in str(err)
    assert namespaces == ['bartender.test']
