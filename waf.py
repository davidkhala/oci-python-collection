import oci.waas as WAF
import oci

config = oci.config.from_file()
wafClient = WAF.WaasClient(config)


