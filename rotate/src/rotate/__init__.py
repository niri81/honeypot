import logging

from rotate.config import Config
from rotate.rotate import rotate
from rotate.utils import construct_path


def main() -> None:
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logger = logging.getLogger(__name__)

    config = Config.from_yaml(construct_path("config.yaml"))
    logger.info("Loaded config")

    rotate(config)
