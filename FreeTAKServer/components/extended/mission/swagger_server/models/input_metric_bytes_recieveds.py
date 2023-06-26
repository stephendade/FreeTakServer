# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InputMetricBytesRecieveds(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, opaque: int=None, acquire: int=None, release: int=None, and_increment: int=None, and_decrement: int=None, plain: int=None):  # noqa: E501
        """InputMetricBytesRecieveds - a model defined in Swagger

        :param opaque: The opaque of this InputMetricBytesRecieveds.  # noqa: E501
        :type opaque: int
        :param acquire: The acquire of this InputMetricBytesRecieveds.  # noqa: E501
        :type acquire: int
        :param release: The release of this InputMetricBytesRecieveds.  # noqa: E501
        :type release: int
        :param and_increment: The and_increment of this InputMetricBytesRecieveds.  # noqa: E501
        :type and_increment: int
        :param and_decrement: The and_decrement of this InputMetricBytesRecieveds.  # noqa: E501
        :type and_decrement: int
        :param plain: The plain of this InputMetricBytesRecieveds.  # noqa: E501
        :type plain: int
        """
        self.swagger_types = {
            'opaque': int,
            'acquire': int,
            'release': int,
            'and_increment': int,
            'and_decrement': int,
            'plain': int
        }

        self.attribute_map = {
            'opaque': 'opaque',
            'acquire': 'acquire',
            'release': 'release',
            'and_increment': 'andIncrement',
            'and_decrement': 'andDecrement',
            'plain': 'plain'
        }
        self._opaque = opaque
        self._acquire = acquire
        self._release = release
        self._and_increment = and_increment
        self._and_decrement = and_decrement
        self._plain = plain

    @classmethod
    def from_dict(cls, dikt) -> 'InputMetricBytesRecieveds':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InputMetric_bytesRecieveds of this InputMetricBytesRecieveds.  # noqa: E501
        :rtype: InputMetricBytesRecieveds
        """
        return util.deserialize_model(dikt, cls)

    @property
    def opaque(self) -> int:
        """Gets the opaque of this InputMetricBytesRecieveds.


        :return: The opaque of this InputMetricBytesRecieveds.
        :rtype: int
        """
        return self._opaque

    @opaque.setter
    def opaque(self, opaque: int):
        """Sets the opaque of this InputMetricBytesRecieveds.


        :param opaque: The opaque of this InputMetricBytesRecieveds.
        :type opaque: int
        """

        self._opaque = opaque

    @property
    def acquire(self) -> int:
        """Gets the acquire of this InputMetricBytesRecieveds.


        :return: The acquire of this InputMetricBytesRecieveds.
        :rtype: int
        """
        return self._acquire

    @acquire.setter
    def acquire(self, acquire: int):
        """Sets the acquire of this InputMetricBytesRecieveds.


        :param acquire: The acquire of this InputMetricBytesRecieveds.
        :type acquire: int
        """

        self._acquire = acquire

    @property
    def release(self) -> int:
        """Gets the release of this InputMetricBytesRecieveds.


        :return: The release of this InputMetricBytesRecieveds.
        :rtype: int
        """
        return self._release

    @release.setter
    def release(self, release: int):
        """Sets the release of this InputMetricBytesRecieveds.


        :param release: The release of this InputMetricBytesRecieveds.
        :type release: int
        """

        self._release = release

    @property
    def and_increment(self) -> int:
        """Gets the and_increment of this InputMetricBytesRecieveds.


        :return: The and_increment of this InputMetricBytesRecieveds.
        :rtype: int
        """
        return self._and_increment

    @and_increment.setter
    def and_increment(self, and_increment: int):
        """Sets the and_increment of this InputMetricBytesRecieveds.


        :param and_increment: The and_increment of this InputMetricBytesRecieveds.
        :type and_increment: int
        """

        self._and_increment = and_increment

    @property
    def and_decrement(self) -> int:
        """Gets the and_decrement of this InputMetricBytesRecieveds.


        :return: The and_decrement of this InputMetricBytesRecieveds.
        :rtype: int
        """
        return self._and_decrement

    @and_decrement.setter
    def and_decrement(self, and_decrement: int):
        """Sets the and_decrement of this InputMetricBytesRecieveds.


        :param and_decrement: The and_decrement of this InputMetricBytesRecieveds.
        :type and_decrement: int
        """

        self._and_decrement = and_decrement

    @property
    def plain(self) -> int:
        """Gets the plain of this InputMetricBytesRecieveds.


        :return: The plain of this InputMetricBytesRecieveds.
        :rtype: int
        """
        return self._plain

    @plain.setter
    def plain(self, plain: int):
        """Sets the plain of this InputMetricBytesRecieveds.


        :param plain: The plain of this InputMetricBytesRecieveds.
        :type plain: int
        """

        self._plain = plain
