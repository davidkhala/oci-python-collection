# /documents/api/1.2/folders/{folderId}


class Base:
    tenancy_name: str
    instance_name: str

    def __init__(self, tenancy_name: str, instance_name: str):
        self.tenancy_name = tenancy_name
        self.instance_name = instance_name

    def url(self):
        return "{}-{}.cec.ocp.oraclecloud.com".format(self.instance_name, self.tenancy_name)

    def login(self):
        
            # https://cx-hktwlab.cec.ocp.oraclecloud.com/documents/web?IdcService=GET_OAUTH_TOKEN
        return 2
