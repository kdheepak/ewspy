from .soap_request import NAMESPACES, elem2dict


def get_room_lists(root):

    roomlist_list = []
    for element in root.xpath('//t:Address', namespaces=NAMESPACES):
        roomlist_dict = elem2dict(element)
        roomlist_list.append(roomlist_dict)

    return roomlist_list


def get_rooms(root):

    rooms_list = []
    for element in root.xpath('//t:Room/t:Id', namespaces=NAMESPACES):
        room = elem2dict(element)
        rooms_list.append(room)

    return rooms_list


def get_availability(root):

    event_list = []
    for element in root.xpath('//t:CalendarEvent', namespaces=NAMESPACES):
        event = elem2dict(element)
        event_list.append(event)

    return event_list
