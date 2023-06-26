# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class VersionInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, major: int=None, minor: int=None, patch: int=None, branch: str=None, variant: str=None):  # noqa: E501
        """VersionInfo - a model defined in Swagger

        :param major: The major of this VersionInfo.  # noqa: E501
        :type major: int
        :param minor: The minor of this VersionInfo.  # noqa: E501
        :type minor: int
        :param patch: The patch of this VersionInfo.  # noqa: E501
        :type patch: int
        :param branch: The branch of this VersionInfo.  # noqa: E501
        :type branch: str
        :param variant: The variant of this VersionInfo.  # noqa: E501
        :type variant: str
        """
        self.swagger_types = {
            'major': int,
            'minor': int,
            'patch': int,
            'branch': str,
            'variant': str
        }

        self.attribute_map = {
            'major': 'major',
            'minor': 'minor',
            'patch': 'patch',
            'branch': 'branch',
            'variant': 'variant'
        }
        self._major = major
        self._minor = minor
        self._patch = patch
        self._branch = branch
        self._variant = variant

    @classmethod
    def from_dict(cls, dikt) -> 'VersionInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VersionInfo of this VersionInfo.  # noqa: E501
        :rtype: VersionInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def major(self) -> int:
        """Gets the major of this VersionInfo.


        :return: The major of this VersionInfo.
        :rtype: int
        """
        return self._major

    @major.setter
    def major(self, major: int):
        """Sets the major of this VersionInfo.


        :param major: The major of this VersionInfo.
        :type major: int
        """

        self._major = major

    @property
    def minor(self) -> int:
        """Gets the minor of this VersionInfo.


        :return: The minor of this VersionInfo.
        :rtype: int
        """
        return self._minor

    @minor.setter
    def minor(self, minor: int):
        """Sets the minor of this VersionInfo.


        :param minor: The minor of this VersionInfo.
        :type minor: int
        """

        self._minor = minor

    @property
    def patch(self) -> int:
        """Gets the patch of this VersionInfo.


        :return: The patch of this VersionInfo.
        :rtype: int
        """
        return self._patch

    @patch.setter
    def patch(self, patch: int):
        """Sets the patch of this VersionInfo.


        :param patch: The patch of this VersionInfo.
        :type patch: int
        """

        self._patch = patch

    @property
    def branch(self) -> str:
        """Gets the branch of this VersionInfo.


        :return: The branch of this VersionInfo.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch: str):
        """Sets the branch of this VersionInfo.


        :param branch: The branch of this VersionInfo.
        :type branch: str
        """

        self._branch = branch

    @property
    def variant(self) -> str:
        """Gets the variant of this VersionInfo.


        :return: The variant of this VersionInfo.
        :rtype: str
        """
        return self._variant

    @variant.setter
    def variant(self, variant: str):
        """Sets the variant of this VersionInfo.


        :param variant: The variant of this VersionInfo.
        :type variant: str
        """

        self._variant = variant
