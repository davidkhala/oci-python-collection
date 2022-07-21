# /documents/api/1.2/folders/{folderId}
from http_request import get


class Base:
    tenancy_name: str
    instance_name: str

    def __init__(self, tenancy_name: str, instance_name: str):
        self.tenancy_name = tenancy_name
        self.instance_name = instance_name

    def url(self):
        return "{}-{}.cec.ocp.oraclecloud.com".format(self.instance_name, self.tenancy_name)


    def login(self, tokenValue):
        url = 'https://cx-hktwlab.cec.ocp.oraclecloud.com/documents/api/1.2/folders/items'
        return get('https://cx-hktwlab.cec.ocp.oraclecloud.com/documents/web?IdcService=GET_OAUTH_TOKEN')
