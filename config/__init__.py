import yaml


# load the configuration
with open("config.yml", 'r') as config_file:
    config = yaml.safe_load(config_file)
