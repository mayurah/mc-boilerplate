from pprint import pprint

import arrow

from utils import cli_parser
from utils.config import Config
from trustar import TruStar
from trustar2 import TruStar as TruStar2
from trustar2 import log

logger = log.get_logger(__name__)


def build_config(config_file_path, context):
    return Config(config_file_path, context)


def init_ts_client(config):
    return TruStar(config=config.to_dict())


def init_ts_client2(config):
    return TruStar2(api_key=config.api_key,api_secret=config.api_secret,client_metatag=config.client_metatag)


def main():
    cli_args = cli_parser.parse_cli_args()

    legacy_config = build_config(cli_args.config_file_path, 'legacy')
    ts = init_ts_client(legacy_config)
    logger.info(f"Response TS 1.3: {ts.ping()}")

    workflow_config = build_config(cli_args.config_file_path, 'workflows')
    ts2 = init_ts_client2(workflow_config)
    ping = ts2.account().ping()
    logger.info(f"Response TS 2.0: {ts2.account().ping().data}")
    #
    # enclaves = ts2.account().get_enclaves()
    #
    # for enclave in enclaves.data:
    #     print(f"Name: {enclave.name} - Id:{enclave.id}")
    #
    # response = ts2 \
    #     .indicators() \
    #     .set_enclave_ids(["7a963e2b-3d62-4430-b3bb-7e8c89808fab"]) \
    #     .search()
    #
    # for page in response:
    #     indicators = page.data
    #     for ioc in indicators:
    #         print(f"Type: {ioc.observable.type} - Value: {ioc.observable.value} - Score: {ioc.priority_score}")
    #         if any(x for x in ioc.attributes if x.type == 'MALWARE'):
    #             print(ioc.attributes)

