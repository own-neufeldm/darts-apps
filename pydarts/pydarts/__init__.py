import logging
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

package_dir = Path(__file__).parent
logger = logging.getLogger(__package__)
try:
    __version__ = version(__package__)
except PackageNotFoundError:
    # package is not installed
    pass


def configure_logging(debug: bool) -> None:
    """
    Configure package-level logging.
    """
    level = logging.DEBUG if debug else logging.INFO
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(handler)
    return None
