from __future__ import absolute_import, division, print_function, unicode_literals

from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)

import logging

import requests
from lxml.builder import ElementMaker
from lxml import etree
from requests_ntlm import HttpNtlmAuth

from .exception import EWSException

SOAP_NS = u'http://schemas.xmlsoap.org/soap/envelope/'
TYPE_NS = u'http://schemas.microsoft.com/exchange/services/2006/types'

SOAP_NAMESPACES = {u't': TYPE_NS, u's': SOAP_NS}

S = ElementMaker(namespace=SOAP_NS, nsmap=SOAP_NAMESPACES)
T = ElementMaker(namespace=TYPE_NS, nsmap=SOAP_NAMESPACES)


class EWSSession(requests.Session):

    def __init__(self, url, username=None, password=None, auth=None, encoding="utf-8"):
        super().__init__()
        self.logger = logging.getLogger(__file__)

        self.url = url
        self.encoding = encoding
        self.headers = {"Accept": "text/xml",
                      "Content-type": "text/xml; charset={} ".format(self.encoding)}

        self.auth = auth or HttpNtlmAuth(username, password)

    def post(self, body, url=None, headers=None, auth=None, verify=True, **kwargs):
        url = url or self.url
        headers = headers or self.headers
        auth = auth or self.auth

        body = self._build_xml(body)
        response = super().post(url, data=body, headers=headers, auth=auth, verify=verify, **kwargs)
        response.raise_for_status()

        return self._process_soap_response(response)

    def _process_soap_response(self, response):
        tree = etree.XML(response.content)
        fault_nodes = tree.xpath(u'//s:Fault', namespaces=SOAP_NAMESPACES)
        if fault_nodes:
            raise EWSException(etree.tostring(fault_nodes[0]))
        return tree

    def _exchange_header(self):
        return T.RequestServerVersion({u'Version': u'Exchange2010'})

    def _build_xml(self, body):
        root = S.Envelope(S.Header(self._exchange_header()), S.Body(body))
        body = etree.tostring(root, pretty_print=True, encoding=self.encoding)
        return body
