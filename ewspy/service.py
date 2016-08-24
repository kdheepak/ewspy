from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)

from datetime import datetime
import time
from pytz import timezone, utc

from .session import EWSSession
from .exception import EWSException

from . import builder
from . import parser


class EWSService(object):

    def __init__(self, session):
        self._session = session

    def GetRoomLists(self):
        response = self._session.post(builder.GetRoomLists())
        return parser.GetRoomLists(response)

    def GetRooms(self, email):
        response = self._session.post(builder.GetRooms(email))
        return parser.GetRooms(response)

    def GetUserAvailabilityRequest(self, email, starttime=None, endtime=None, tz="America/Denver"):
        local_tz = timezone(tz)

        if starttime is None:
            now = datetime.now()
            starttime = datetime(now.year, now.month, now.day, 0, 0, 0)
            starttime = local_tz.localize(starttime)

        if endtime is None:
            now = datetime.now()
            endtime = datetime(now.year, now.month, now.day + 1)
            endtime = local_tz.localize(endtime)

        response = self._session.post(builder.GetUserAvailabilityRequest(email, starttime, endtime))
        return parser.GetUserAvailabilityRequest(response)
