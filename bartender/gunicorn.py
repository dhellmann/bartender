"""Load a PathDispatcher using settings from the environment.

The namespace is taken from ``BARTENDER_NAMESPACE`` with a default
of "bartender".
"""

import logging
import os

from bartender.path import PathDispatcher

LOG = logging.getLogger(__name__)

namespace = os.environ.get('BARTENDER_NAMESPACE', 'bartender')
LOG.info('Creating dispatcher with namespace %r', namespace)
app = PathDispatcher(namespace)
