# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.federate_ca_group_association import FederateCAGroupAssociation  # noqa: F401,E501
from swagger_server import util


class ApiResponseListFederateCAGroupAssociation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, version: str=None, type: str=None, data: List[FederateCAGroupAssociation]=None, messages: List[str]=None, node_id: str=None):  # noqa: E501
        """ApiResponseListFederateCAGroupAssociation - a model defined in Swagger

        :param version: The version of this ApiResponseListFederateCAGroupAssociation.  # noqa: E501
        :type version: str
        :param type: The type of this ApiResponseListFederateCAGroupAssociation.  # noqa: E501
        :type type: str
        :param data: The data of this ApiResponseListFederateCAGroupAssociation.  # noqa: E501
        :type data: List[FederateCAGroupAssociation]
        :param messages: The messages of this ApiResponseListFederateCAGroupAssociation.  # noqa: E501
        :type messages: List[str]
        :param node_id: The node_id of this ApiResponseListFederateCAGroupAssociation.  # noqa: E501
        :type node_id: str
        """
        self.swagger_types = {
            'version': str,
            'type': str,
            'data': List[FederateCAGroupAssociation],
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
    def from_dict(cls, dikt) -> 'ApiResponseListFederateCAGroupAssociation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ApiResponseListFederateCAGroupAssociation of this ApiResponseListFederateCAGroupAssociation.  # noqa: E501
        :rtype: ApiResponseListFederateCAGroupAssociation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def version(self) -> str:
        """Gets the version of this ApiResponseListFederateCAGroupAssociation.


        :return: The version of this ApiResponseListFederateCAGroupAssociation.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this ApiResponseListFederateCAGroupAssociation.


        :param version: The version of this ApiResponseListFederateCAGroupAssociation.
        :type version: str
        """

        self._version = version

    @property
    def type(self) -> str:
        """Gets the type of this ApiResponseListFederateCAGroupAssociation.


        :return: The type of this ApiResponseListFederateCAGroupAssociation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ApiResponseListFederateCAGroupAssociation.


        :param type: The type of this ApiResponseListFederateCAGroupAssociation.
        :type type: str
        """

        self._type = type

    @property
    def data(self) -> List[FederateCAGroupAssociation]:
        """Gets the data of this ApiResponseListFederateCAGroupAssociation.


        :return: The data of this ApiResponseListFederateCAGroupAssociation.
        :rtype: List[FederateCAGroupAssociation]
        """
        return self._data

    @data.setter
    def data(self, data: List[FederateCAGroupAssociation]):
        """Sets the data of this ApiResponseListFederateCAGroupAssociation.


        :param data: The data of this ApiResponseListFederateCAGroupAssociation.
        :type data: List[FederateCAGroupAssociation]
        """

        self._data = data

    @property
    def messages(self) -> List[str]:
        """Gets the messages of this ApiResponseListFederateCAGroupAssociation.


        :return: The messages of this ApiResponseListFederateCAGroupAssociation.
        :rtype: List[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages: List[str]):
        """Sets the messages of this ApiResponseListFederateCAGroupAssociation.


        :param messages: The messages of this ApiResponseListFederateCAGroupAssociation.
        :type messages: List[str]
        """

        self._messages = messages

    @property
    def node_id(self) -> str:
        """Gets the node_id of this ApiResponseListFederateCAGroupAssociation.


        :return: The node_id of this ApiResponseListFederateCAGroupAssociation.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id: str):
        """Sets the node_id of this ApiResponseListFederateCAGroupAssociation.


        :param node_id: The node_id of this ApiResponseListFederateCAGroupAssociation.
        :type node_id: str
        """

        self._node_id = node_id
