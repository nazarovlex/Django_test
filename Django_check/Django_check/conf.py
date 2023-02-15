import yaml
config = yaml.load(open("conf.yaml"), Loader=yaml.Loader)
secret_key = config["secret_key"]
