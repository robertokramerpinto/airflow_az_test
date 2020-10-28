from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication

def get_workspace():

    subscription_id = "974f9871-2375-47c7-bfd5-54e55b74fbdd"
    resource_group = "cloudgurutraining"
    workspace_name = "test_1"
    my_application_id = "e8f02d4d-9d0b-4abb-93ed-ed365ebee25f"
    my_tenant_id = "e2c5fd58-d9bc-4c31-9495-bad58ae11f15"
    secret = "_w_pL4RF5h.4FKysfN3.dlqtM~X-2aNtT1"

    svc_pr = ServicePrincipalAuthentication(
        tenant_id=my_tenant_id,
        service_principal_id=my_application_id,
        service_principal_password=secret)

    ws = Workspace(
        subscription_id=subscription_id,
        resource_group=resource_group,
        workspace_name=workspace_name,
        auth=svc_pr
    )
    return ws

