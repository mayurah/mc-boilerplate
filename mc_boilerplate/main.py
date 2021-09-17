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
    logger.info(f"Response TS 2.0: {ts2.account().ping().text}")
