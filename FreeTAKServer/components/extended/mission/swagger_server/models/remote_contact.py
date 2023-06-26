# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RemoteContact(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, contact_name: str=None, last_heard_from_millis: int=None, endpoint: str=None, uid: str=None):  # noqa: E501
        """RemoteContact - a model defined in Swagger

        :param contact_name: The contact_name of this RemoteContact.  # noqa: E501
        :type contact_name: str
        :param last_heard_from_millis: The last_heard_from_millis of this RemoteContact.  # noqa: E501
        :type last_heard_from_millis: int
        :param endpoint: The endpoint of this RemoteContact.  # noqa: E501
        :type endpoint: str
        :param uid: The uid of this RemoteContact.  # noqa: E501
        :type uid: str
        """
        self.swagger_types = {
            'contact_name': str,
            'last_heard_from_millis': int,
            'endpoint': str,
            'uid': str
        }

        self.attribute_map = {
            'contact_name': 'contactName',
            'last_heard_from_millis': 'lastHeardFromMillis',
            'endpoint': 'endpoint',
            'uid': 'uid'
        }
        self._contact_name = contact_name
        self._last_heard_from_millis = last_heard_from_millis
        self._endpoint = endpoint
        self._uid = uid

    @classmethod
    def from_dict(cls, dikt) -> 'RemoteContact':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RemoteContact of this RemoteContact.  # noqa: E501
        :rtype: RemoteContact
        """
        return util.deserialize_model(dikt, cls)

    @property
    def contact_name(self) -> str:
        """Gets the contact_name of this RemoteContact.


        :return: The contact_name of this RemoteContact.
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name: str):
        """Sets the contact_name of this RemoteContact.


        :param contact_name: The contact_name of this RemoteContact.
        :type contact_name: str
        """

        self._contact_name = contact_name

    @property
    def last_heard_from_millis(self) -> int:
        """Gets the last_heard_from_millis of this RemoteContact.


        :return: The last_heard_from_millis of this RemoteContact.
        :rtype: int
        """
        return self._last_heard_from_millis

    @last_heard_from_millis.setter
    def last_heard_from_millis(self, last_heard_from_millis: int):
        """Sets the last_heard_from_millis of this RemoteContact.


        :param last_heard_from_millis: The last_heard_from_millis of this RemoteContact.
        :type last_heard_from_millis: int
        """

        self._last_heard_from_millis = last_heard_from_millis

    @property
    def endpoint(self) -> str:
        """Gets the endpoint of this RemoteContact.


        :return: The endpoint of this RemoteContact.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint: str):
        """Sets the endpoint of this RemoteContact.


        :param endpoint: The endpoint of this RemoteContact.
        :type endpoint: str
        """

        self._endpoint = endpoint

    @property
    def uid(self) -> str:
        """Gets the uid of this RemoteContact.


        :return: The uid of this RemoteContact.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid: str):
        """Sets the uid of this RemoteContact.


        :param uid: The uid of this RemoteContact.
        :type uid: str
        """

        self._uid = uid
