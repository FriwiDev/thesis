import json

from dsmf_server.models.domain_configuration import DomainConfiguration


class ConfigurationUtil(object):
    @classmethod
    def load_configuration_from_disk(cls) -> DomainConfiguration:
        with open('domain_config.json', 'r') as file:
            content = file.read()
            return DomainConfiguration.from_dict(json.loads(content))

    @classmethod
    def save_configuration_to_disk(cls, config: DomainConfiguration):
        with open('domain_config.json', 'rw') as file:
            file.write(config.to_str())
