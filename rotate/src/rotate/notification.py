import apprise


class Notifier:
    def __init__(self, notifier_config: list[str]) -> None:
        self.notifier = apprise.Apprise()
        for line in notifier_config:
            self.notifier.add(line)

    def notify(self, title: str, body: str):
        self.notifier.notify(title=title, body=body)
