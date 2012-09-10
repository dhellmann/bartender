
import logging

LOG = logging.getLogger(__name__)


class TestApp(object):
    """Bartender test application.
    """

    def __init__(self, name):
        self.name = name
        LOG.info('Creating TestApp(%s)', name)

    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-type', 'text/plain')])
        return 'intentionally blank'
