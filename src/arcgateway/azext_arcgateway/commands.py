# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

def load_command_table(self, _):  # pylint: disable=unused-argument
    with self.command_group("arcgateway settings"):
        from .custom import SettingsUpdate
        self.command_table["arcgateway settings update"] = SettingsUpdate(loader=self)