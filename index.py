import oci
config = oci.config.from_file()
identity = oci.identity.IdentityClient(config)
compartment_id = config["tenancy"]
