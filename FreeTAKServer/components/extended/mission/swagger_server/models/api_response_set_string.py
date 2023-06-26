# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ApiResponseSetString(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, version: str=None, type: str=None, data: List[str]=None, messages: List[str]=None, node_id: str=None):  # noqa: E501
        """ApiResponseSetString - a model defined in Swagger

        :param version: The version of this ApiResponseSetString.  # noqa: E501
        :type version: str
        :param type: The type of this ApiResponseSetString.  # noqa: E501
        :type type: str
        :param data: The data of this ApiResponseSetString.  # noqa: E501
        :type data: List[str]
        :param messages: The messages of this ApiResponseSetString.  # noqa: E501
        :type messages: List[str]
        :param node_id: The node_id of this ApiResponseSetString.  # noqa: E501
        :type node_id: str
        """
        self.swagger_types = {
            'version': str,
            'type': str,
            'data': List[str],
            'messages': List[str],
            'node_id': str
        }

        self.attribute_map = {
            'version': 'version',
            'type': 'type',
            'data': 'data',
            'messages': 'messages',
            'node_id': 'nodeId'
        }
        self._version = version
        self._type = type
        self._data = data
        self._messages = messages
        self._node_id = node_id

    @classmethod
    def from_dict(cls, dikt) -> 'ApiResponseSetString':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ApiResponseSetString of this ApiResponseSetString.  # noqa: E501
        :rtype: ApiResponseSetString
        """
        return util.deserialize_model(dikt, cls)

    @property
    def version(self) -> str:
        """Gets the version of this ApiResponseSetString.


        :return: The version of this ApiResponseSetString.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this ApiResponseSetString.


        :param version: The version of this ApiResponseSetString.
        :type version: str
        """

        self._version = version

    @property
    def type(self) -> str:
        """Gets the type of this ApiResponseSetString.


        :return: The type of this ApiResponseSetString.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ApiResponseSetString.


        :param type: The type of this ApiResponseSetString.
        :type type: str
        """

        self._type = type

    @property
    def data(self) -> List[str]:
        """Gets the data of this ApiResponseSetString.


        :return: The data of this ApiResponseSetString.
        :rtype: List[str]
        """
        return self._data

    @data.setter
    def data(self, data: List[str]):
        """Sets the data of this ApiResponseSetString.


        :param data: The data of this ApiResponseSetString.
        :type data: List[str]
        """

        self._data = data

    @property
    def messages(self) -> List[str]:
        """Gets the messages of this ApiResponseSetString.


        :return: The messages of this ApiResponseSetString.
        :rtype: List[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages: List[str]):
        """Sets the messages of this ApiResponseSetString.


        :param messages: The messages of this ApiResponseSetString.
        :type messages: List[str]
        """

        self._messages = messages

    @property
    def node_id(self) -> str:
        """Gets the node_id of this ApiResponseSetString.


        :return: The node_id of this ApiResponseSetString.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id: str):
        """Sets the node_id of this ApiResponseSetString.


        :param node_id: The node_id of this ApiResponseSetString.
        :type node_id: str
        """

        self._node_id = node_id
