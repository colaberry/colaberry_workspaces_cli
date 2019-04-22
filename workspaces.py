import boto3
import constants

session = boto3.Session(
    aws_access_key_id=constants.AWS_ACCESS_KEY,
    aws_secret_access_key=constants.AWS_SECRET_KEY,
    region_name=constants.REGION_NAME
)


def get_workspaces_details(username, indicator):
    client = session.client('workspaces')
    response = client.describe_workspaces(
        DirectoryId=constants.DIRECTORY_ID,
    )

    get_workspace_ids(response, username, indicator)


def get_workspace_ids(res, username, indicator):
    for value in res['Workspaces']:
        if username == value['UserName']:
            control_workspace_id(value['WorkspaceId'], username, indicator)


def stop_workspace_id(value, username):
    client = session.client('workspaces')
    response = client.stop_workspaces(
        StopWorkspaceRequests=[
            {
                'WorkspaceId': value
            }
        ]
    )
    display_cli_message(response, username, indicator='stop')


def start_workspace_id(value, username):
    client = session.client('workspaces')
    response = client.start_workspaces(
        StartWorkspaceRequests=[
            {
                'WorkspaceId': value
            }
        ]
    )
    display_cli_message(response, username, indicator='start')


def control_workspace_id(value, username, indicator):
    return start_workspace_id(value, username) if indicator == 'start' else stop_workspace_id(value, username)


def display_cli_message(response, value, indicator):
    if len(response["FailedRequests"]) == 0:
        print(constants.SUCCESS, 'Workspace:', value, indicator)
    else:
        print(constants.ERROR, value, response['FailedRequests'][0]['ErrorMessage'])
