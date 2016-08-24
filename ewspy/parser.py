from .soap_request import NAMESPACES


def get_room_lists(root):

    roomlist_list = []
    for element in root.xpath('//t:Address', namespaces=NAMESPACES):
        roomlist = {}
        for e in element.getchildren():
            key = e.tag.replace(NAMESPACES['t'], '').replace('{}', '')
            roomlist[key] = e.text
        roomlist_list.append(roomlist)

    return roomlist_list


def get_rooms(root):

    list_of_rooms = []
    for element in root.xpath('//t:Room', namespaces=NAMESPACES):
        room = {}
        for e in element.getchildren()[0].getchildren():
            key = e.tag.replace(NAMESPACES['t'], '').replace('{}', '')
            room[key] = e.text
        list_of_rooms.append(room)

    return list_of_rooms



