from lxml.builder import ElementMaker

MSG_NS = u'http://schemas.microsoft.com/exchange/services/2006/messages'
TYPE_NS = u'http://schemas.microsoft.com/exchange/services/2006/types'
SOAP_NS = u'http://schemas.xmlsoap.org/soap/envelope/'

NAMESPACES = {u'm': MSG_NS, u't': TYPE_NS, u's': SOAP_NS}

M = ElementMaker(namespace=MSG_NS, nsmap=NAMESPACES)
T = ElementMaker(namespace=TYPE_NS, nsmap=NAMESPACES)

EXCHANGE_DATETIME_FORMAT = u"%Y-%m-%dT%H:%M:%SZ"
EXCHANGE_DATE_FORMAT = u"%Y-%m-%d"


def elem2dict(node):
    """
    Convert an lxml.etree node tree into a dict.
    """
    d = {}
    for e in node.iterchildren():
        key = e.tag.split('}')[1] if '}' in e.tag else e.tag
        value = e.text if e.text else elem2dict(e)
        d[key] = value
    return d
