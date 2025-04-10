import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
import platform
from importlib.metadata import distributions
from audio_in import audio_input_factory

def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    """catches unhandled exceptions and logs them"""

    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.critical("Exception", exc_info=(exc_type, exc_value, exc_traceback))
    logging.critical(
        "Unhandled Exception {0}: {1}".format(exc_type, exc_value),
        extra={"exception": "".join(traceback.format_tb(exc_traceback))},
    )


def details() -> str:
    """return details about python version and platform as a dict"""

    platform_details = {
        "python_version": sys.version,
        "platform": sys.platform,
        "platform_details": platform.platform(),
    }

    installed_packages = [(dist.metadata["Name"], dist.version) for dist in distributions()]
    for package in installed_packages:
        platform_details[package[0]] = package[1]

    return platform_details


def str2bool(value: str) -> bool:
    """ converts strings representing truth to bool """ ""
    return value.lower() in ("yes", "true", "t", "1")


def probe(file_path:str) -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f"Invoked test function - TEST_CONFIG={test_config!r}")
    logger.info(f"details={details()}")

    platform_details = details()
    for key in platform_details.keys():
        logger.info(f"{key}: {platform_details[key]}")

    if file_path:
        logger.info(f"file_path={file_path}")
        audio = audio_input_factory(file_path)

        packet_count = 0
        for pcm_bytes in audio.get_audio():
            packet_count += 1
            logger.debug(f"Audio Bytes Processed: {len(pcm_bytes)}, Packet: {packet_count}")

    return 0


def main() -> int:
    """
    main function

    returns 0 on success, 1 on failure

    configures logging and processes command line arguments
    """
    with io.open(f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml") as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description="Audio Prober")
    parser.add_argument("--probe", dest="probe", action="store_true")
    parser.add_argument("--file", dest="file", type=str)
    args = parser.parse_args()

    if not os.path.exists(args.file):
        logging.error(f"File '{args.file}' does not exist")
        return 1
    
    success = 0
    if args.probe:
        success = probe(args.file)
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
