from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
from future.utils import with_metaclass
from types import MethodType

from .session import EWSSession
from .exception import EWSException

class _EWSServicesMeta(type):

    def __new__(meta, name, bases, dct):

        service_class = super().__new__(meta, name, bases, dct)

        for service in dct['_functions']:
            setattr(service_class, service, MethodType(func, None, service_class))

        return service_class


class EWSService(with_metaclass(_EWSServicesMeta)):

    def __init__(self, session=None,
                 url=None,
                 username=None,
                 password=None):

        if session is not None and not isinstance(session, EWSSession):
            raise EWSException('Session has to be of instance EWSSession. Check documentation for more information')

        self._session = EWSSession(url, username, password)



