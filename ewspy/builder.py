from .soap_request import M, T, EXCHANGE_DATETIME_FORMAT


def GetRoomLists():
    return M.GetRoomLists()


def GetRooms(roomlist_email):
    root = M.GetRooms(
        M.RoomList(
            T.EmailAddress(roomlist_email)
        )
    )
    return root


def GetUserAvailabilityRequest(email, starttime, endtime):

    starttime = starttime.strftime(EXCHANGE_DATETIME_FORMAT)
    endtime = endtime.strftime(EXCHANGE_DATETIME_FORMAT)

    root = M.GetUserAvailabilityRequest(
        T.TimeZone(
            T.Bias('360'),
            T.StandardTime(
                T.Bias('0'),
                T.Time('02:00:00'),
                T.DayOrder('5'),
                T.Month('10'),
                T.DayOfWeek('Sunday')
            ),
            T.DaylightTime(
                T.Bias('0'),
                T.Time('02:00:00'),
                T.DayOrder('1'),
                T.Month('4'),
                T.DayOfWeek('Sunday')
            )
        ),
        M.MailboxDataArray(
            T.MailboxData(
                T.Email(
                    T.Address(email)
                ),
                T.AttendeeType('Required'),
                T.ExcludeConflicts('false')
            )
        ),
        T.FreeBusyViewOptions(
            T.TimeWindow(
                T.StartTime(starttime),
                T.EndTime(endtime),
            ),
            T.MergedFreeBusyIntervalInMinutes('60'),
            T.RequestedView('DetailedMerged')
        )
    )

    return root


def GetServerTimeZones(self):
    """
    https://msdn.microsoft.com/en-us/library/office/dd899371(v=exchg.150).aspx
    """
    M.GetServerTimeZones(
        T.Ids()
    )
