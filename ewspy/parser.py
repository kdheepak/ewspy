from .soap_request import NAMESPACES, elem2dict


def GetRoomLists(root):

    roomlist_list = []
    for element in root.xpath('//t:Address', namespaces=NAMESPACES):
        roomlist_dict = elem2dict(element)
        roomlist_list.append(roomlist_dict)

    return roomlist_list


def GetRooms(root):

    rooms_list = []
    for element in root.xpath('//t:Room/t:Id', namespaces=NAMESPACES):
        room = elem2dict(element)
        rooms_list.append(room)

    return rooms_list


def GetUserAvailabilityRequest(root):

    event_list = []
    for element in root.xpath('//t:CalendarEvent', namespaces=NAMESPACES):
        event = elem2dict(element)
        event_list.append(event)

    return event_list
