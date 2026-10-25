from rotate.config import Config
from rotate.notification import Notifier


def main() -> None:
    config = Config.from_yaml("config.yaml")
    notifier = Notifier(config.get("notifiers"))
