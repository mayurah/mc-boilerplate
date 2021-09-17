from argparse import ArgumentParser


def parse_cli_args():
    parser = ArgumentParser(description="TruSTAR Managed Connector")

    parser.add_argument(
        "-c",
        "--config-file",
        dest="config_file_path",
        help="Config file name",
        required=True
    )

    parser.add_argument(
        "-s",
        "--start-time-delta",
        dest="start_time_delta",
        type=int,
        help="Search offset in hours. I.e 6 hours ago"
    )

    return parser.parse_args()
