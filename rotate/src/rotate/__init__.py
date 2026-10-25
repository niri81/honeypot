from rotate.config import Config
from rotate.notification import Notifier
from rotate.rotate import rotate
from rotate.utils import construct_path


def main() -> None:
    config = Config.from_yaml(construct_path("config.yaml"))
    notifier = Notifier(config.get("notifiers"))
    rotate(config)
