# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class CatalogItemType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of catalog item used to deploy the environment.
    """

    ARM = "ARM"

class OsType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The operating system type.
    """

    WINDOWS = "Windows"