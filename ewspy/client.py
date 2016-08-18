from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)

from .service import EWSService
from .exception import EWSException


class EWSClient(object):

    def __init__(self, service):

        if not isinstance(service, EWSService):
            raise EWSException('Service has to be of instance EWSService. Check documentation for more information')

        self._service = service

