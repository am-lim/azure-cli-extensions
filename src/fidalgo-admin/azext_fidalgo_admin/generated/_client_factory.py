# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_fidalgo_admin_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_fidalgo_admin.vendored_sdks.fidalgo_admin import Fidalgo
    return get_mgmt_service_client(cli_ctx,
                                   Fidalgo)


def cf_dev_center(cli_ctx, *_):
    return cf_fidalgo_admin_cl(cli_ctx).dev_centers


def cf_project(cli_ctx, *_):
    return cf_fidalgo_admin_cl(cli_ctx).projects


def cf_environment(cli_ctx, *_):
    return cf_fidalgo_admin_cl(cli_ctx).environments


def cf_deployment(cli_ctx, *_):
    return cf_fidalgo_admin_cl(cli_ctx).deployments


def cf_environment_type(cli_ctx, *_):
    return cf_fidalgo_admin_cl(cli_ctx).environment_types


def cf_catalog_item(cli_ctx, *_):
    return cf_fidalgo_admin_cl(cli_ctx).catalog_items


def cf_catalog(cli_ctx, *_):
    return cf_fidalgo_admin_cl(cli_ctx).catalogs


def cf_mapping(cli_ctx, *_):
    return cf_fidalgo_admin_cl(cli_ctx).mappings


def cf_operation_statuses(cli_ctx, *_):
    return cf_fidalgo_admin_cl(cli_ctx).operation_statuses


def cf_sku(cli_ctx, *_):
    return cf_fidalgo_admin_cl(cli_ctx).skus


def cf_pool(cli_ctx, *_):
    return cf_fidalgo_admin_cl(cli_ctx).pools


def cf_machine_definition(cli_ctx, *_):
    return cf_fidalgo_admin_cl(cli_ctx).machine_definitions


def cf_network_setting(cli_ctx, *_):
    return cf_fidalgo_admin_cl(cli_ctx).network_settings