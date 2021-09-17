import json
from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    def __init__(self, config_file_path=None, context=None):
        self.config_file = config_file_path
        self.context = context

        self.api_key = None
        self.api_secret = None
        self.client_metatag = None
        self.enclaves = []

        if context:
            self.generate_config()

    def set_context(self, context):
        self.context = context

    def generate_config(self):
        with open(self.config_file, "r") as f:
            config_file = json.load(f)

        config = config_file.get(self.context)
        if not config:
            raise AttributeError(
                f"Context: {self.context} not found in {self.config_file}."
            )
        self.api_key = os.getenv(config['api_key'], config['api_key'])
        self.api_secret = os.getenv(config['api_secret'], config['api_secret'])
        self.client_metatag = os.getenv(config['client_metatag'], config['client_metatag'])
        self.enclaves.extend(config['enclave_ids'])

    def to_dict(self):
        return {
            'api_key': self.api_key,
            'api_secret': self.api_secret,
            'client_metatag': self.client_metatag,
            'enclaves': self.enclaves
        }
