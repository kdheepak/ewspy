from __future__ import absolute_import, division, print_function, unicode_literals

from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)

import logging

import requests
from lxml import etree
from requests_ntlm import HttpNtlmAuth

from .exception import EWSException

SOAP_NS = u'http://schemas.xmlsoap.org/soap/envelope/'
SOAP_NAMESPACES = {u's': SOAP_NS}


class EWSSession(requests.Session):

    def __init__(self, url, username=None, password=None, auth=None):
        self.logger = logging.getLogger(__file__)
        self.url = url
        self.auth = auth or HttpNtlmAuth(username, password)
        super().__init__()

    def post(self, body, url=None, headers=None, auth=None):
        url = url or self.url
        headers = headers or self.headers
        auth = auth or self.auth

        body = etree.tostring(body, pretty_print=True)

        response = super().post(url, data=body, headers=headers, auth=auth)

        return response

    def _process_soap_response(self, response):
        tree = etree.XML(response.content)
        fault_nodes = tree.xpath(u'//s:Fault', namespaces=SOAP_NAMESPACES)
        if fault_nodes:
            raise EWSException(etree.tostring(fault_nodes[0]))
        response.raise_for_status()
        return tree

