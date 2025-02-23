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
import av
from measure import measure
from normalise import normalise
from concatenate import build


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


def test(folder: str, operation: str, output: str) -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f"Invoked test function - TEST_CONFIG={test_config!r}")
    # logger.info(f"details={details()}")
    # platform_details = details()
    # for key in platform_details.keys():
    #     logger.info(f"{key}: {platform_details[key]}")

    if operation == "measure":
        measure(folder)
    elif operation == "normalise":
        normalise(folder, output)
    elif operation == "concatenate":
        build(folder, os.path.join(output, "output.wav"))
    else:
        logger.error(f"Unknown operation: {operation}")
    
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

    parser = argparse.ArgumentParser(description="Number Station Builder")
    parser.add_argument("--folder", dest="folder", type=str)
    parser.add_argument("--output", dest="output", type=str)
    parser.add_argument("--operation", dest="operation", type=str)
    args = parser.parse_args()

    success = 0
    if args.operation:
        success = test(args.folder, args.operation, args.output)
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
