import json
def get_env():
    """This function fetch the user email id from databricks config. 
    And returns 'PPE' if emailid endswith ppe.ae and 'PROD' if not ends with ppe.ae """
    clusters_config = dbutils.entry_point.getDbutils().notebook().getContext().toJson()
    env_flag = json.loads(clusters_config)['tags']['user'].endswith('ppe.ae')
    if env_flag:
        env = 'PPE'
    else:
        env = 'PROD'
    return env

"""
Below is the dbutils command which provides details related to notebook and all.
dbutils.entry_point.getDbutils().notebook().getContext().toJson()
Output:
{'rootRunId': None,
 'currentRunId': None,
 'jobGroup': 'xxxxxxx_xxxxxx_adxxxxxxx',
 'tags': {'opId': 'ServerBackend-xxxxx',
  'shardName': 'az-xxxxx',
  'opTarget': 'com.databricks.backend.common.rpc.InternalDriverBackendMessages$StartRepl',
  'notebookEditorNodeType': 'shell',
  'clusterMemory': '28672',
  'serverBackendName': 'com.databricks.backend.daemon.driver.DriverCorral',
  'notebookId': 'xxxxxx',
  'projectName': 'xxxxx',
  'tier': 'tier-multitenant',
  'eventWindowTime': 'xxxxx.399999857',
  'httpTarget': '/notebook/xxxxxx',
  'commandRunId': 'xxxx-xxxx-xxxx-xxxxx-xxxxx',
  'buildHash': '',
  'workspaceRoutingTarget': 'DESTINATION_DB',
  'browserHash': '#notebook/xxxxxx/command/xxxxxx',
  'host': 'xxx.xxx.xxx.xx',
  'browserPathName': '/',
  'notebookLanguage': 'python',
  'workspaceRoutingBucket': 'null',
  'sparkVersion': '11.3.x-scala2.12',
  'hostName': 'xxx-webapp-3',
  'httpMethod': 'POST',
  'browserIdleTime': '273',
  'jettyRpcJettyVersion': '9',
  'browserLanguage': 'en-US',
  'browserTabId': '580b229e-d0e9-4543-9262-9b0cd07de86b',
  'sourceIpAddress': 'xxx.xxx.xxx.xxx',
  'accountId': 'xxxxx-xxxx-xxxx-xxx-xxxxx',
  'loadedUiVersions': 'Map(monolith -> 872f16d25d14e526230685fc08ad6a46ebf0e16a)',
  'browserUserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'orgId': 'xxxx',
  'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'clusterId': 'xxxx-xxxx-xxxx',
  'databricks.notebook.sqlWarehouseNotebookShouldFailOnUnsupportedCommand': 'true',
  'workloadClass': 'commandRun',
  'serverEventId': 'CgwIiLyjrgYQwIHgvXXXXXXXXpQbOJ8hMmi1',
  'rootOpId': 'ServiceMain-xxxx',
  'sessionId': '',
  'clusterCreator': 'xxxxx@gmail.com',
  'originatedFromEnvoy': 'true',
  'clientBranchName': 'webapp_2024-02-07_23.01.09Z_webapp-hotfix-20240207_d0590e1e_1200357324',
  'workloadId': '',
  'clientTimestamp': '1707665531658',
  'clusterType': 'spot',
  'requestId': 'ServiceMain-xxxx',
  'browserHasFocus': 'true',
  'queryParameters': '?o=xxxxxx',
  'userId': '',
  'browserIsHidden': 'false',
  'principalIdpId': 'xxxxx-xxxx-xxxx-xxxx-xxxxx',
  'clientLocale': 'en',
  'branchName': '',
  'opType': 'ServerBackend',
  'sourcePortNumber': '0',
  'user': 'xxxxx@gmail.com',
  'principalIdpObjectId': '',
  'browserHostName': 'adb-xxxxx.10.azuredatabricks.net',
  'parentOpId': 'RPCClient-c82cabda03695e5d',
  'jettyRpcType': 'InternalDriverBackendMessages$DriverBackendRequest'},
 'extraContext': {'mlflowGitRelativePath': '<notebook_name>',
  'allowStdin': 'true',
  'non_uc_api_token': '',
  'commandResultJsonMaxBytes': '20971520',
  'enableDeltaLiveTablesAnalysis': 'true',
  'mlflowGitStatus': 'unknown',
  'mlflowGitReference': '',
  'mlflowGitUrl': 'https://<repo>@dev.azure.com/<repo>/<repo>/_git/<git_repo>',
  'notebook_path': '',
  'notebook_id': 'xxxxxxx',
  'thresholdForStoringInDbfs': '10000',
  'mlflowGitCommit': '',
  'enableStoringResultsInDbfs': 'true',
  'mlflowGitReferenceType': 'branch',
  'api_url': 'https://xxx.azuredatabricks.net',
  'aclPathOfAclRoot': '/workspace/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx',
  'mlflowGitProvider': 'azureDevOpsServices',
  'api_token': '<token>'},
 'credentialKeys': []}
"""
