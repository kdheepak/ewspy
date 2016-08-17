from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)

from .session import EWSSession
from .exception import EWSException


class EWSClient(object):

    def __init__(self, session=None,
                 url=None,
                 username=None,
                 password=None):

        if session is not None and not isinstance(session, EWSSession):
            raise EWSException('Session has to be of instance EWSSession. Check documentation for more information')

        self._session = EWSSession(url, username, password)
