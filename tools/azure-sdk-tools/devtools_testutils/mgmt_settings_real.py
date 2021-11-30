# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os

CLIENT_ID = os.environ.get("CLIENT_ID", None)
SUBSCRIPTION_KEY = os.environ.get("SUBSCRIPTION_KEY")

ENABLE_LOGGING = True

# Read for details of this file:
# https://github.com/Azure/azure-sdk-for-python/wiki/Contributing-to-the-tests

def get_azure_core_credentials(**kwargs):
    from azure.core.credentials import AzureKeyCredential
    from azure.core.pipeline.policies import AzureKeyCredentialPolicy

    credential = AzureKeyCredential(SUBSCRIPTION_KEY)
    return AzureKeyCredentialPolicy(name="subscription-key", credential=credential)

    #from azure.identity import ClientSecretCredential
    #return ClientSecretCredential(
    #    client_id = os.environ['CLIENT_ID'],
    #    client_secret = os.environ['SUBSCRIPTION_KEY'],
    #    tenant_id = os.environ['TENANT_ID']
    #)


def get_credentials(**kwargs):
    from azure.common.credentials import BasicTokenAuthentication, UserPassCredentials

    # Put your credentials here in the "real" file
    # return UserPassCredentials(
    #    'user@myaddomain.onmicrosoft.com',
    #    'Password'
    # )
    # note that UserCredential does not work any longer. Must use a ServicePrincipal.
    # for deprecated APIs I believe will still work.
    # return ServicePrincipalCredentials(
    #     client_id = '<AAD App client id>',
    #     secret = '<secret for the aad app>',
    #     tenant = '<microsoft aad tenant id>'
    # )
    # Needed to play recorded tests
    return BasicTokenAuthentication(token={"access_token": "faked_token"})
