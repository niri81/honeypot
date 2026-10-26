import json
import logging

from rotate.config import Config
from rotate.docker import (
    container_compose_down,
    container_compose_up,
    container_diff_against_baseline,
    container_export_by_id,
    container_get_id_by_name,
)
from rotate.logs import delete_logs, save_logs_and_fs
from rotate.notification import Notifier
from rotate.utils import construct_path

logger = logging.getLogger(__name__)


def rotate(config: Config):
    log_path = construct_path(config.get("log_path"))

    for container in config.get("containers"):
        container_name = container.get("name")
        if not container_name:
            raise ValueError(
                f"Container name not defined in config, received container: {container}"
            )

        logger.info(f"Now rotating container {container_name}")

        container_id = container_get_id_by_name(container_name)

        falco_log_path = construct_path(
            config.get("falco_log_path"), check_exists=False
        )
        falco_logs = ""
        if falco_log_path.exists():
            with open(falco_log_path, "r") as f:
                falco_logs = f.read()

        notifier = Notifier(config.get("notifiers"))

        needs_save = False

        if container_name in falco_logs or container_id in falco_logs:
            logger.info("Detected container mention in Falco logs")

            needs_save = True
            notifier.notify(
                f"Got Falco Logs for Container {container_name}",
                "\n".join(
                    [
                        line
                        for line in falco_logs.splitlines()
                        if container_name in line or container_id in line
                    ]
                ).strip(),
            )

        diff = container_diff_against_baseline(
            container_id, container.get("baseline") or ""
        )
        logger.info(f"Diff between container and baseline is: {json.dumps(diff)}")
        if diff := any(diff.values()):
            needs_save = True
            notifier.notify(
                f"Diff Detected for Container {container_name}", json.dumps(diff)
            )

        if needs_save:
            container_export_by_id(
                container_id,
                output_dir=log_path / f"container_{container_name}_fs.tar",
            )

            save_logs_and_fs(
                log_path,
                container.get("log_path_suffix"),
                construct_path(config.get("output_path")),
                container_name,
            )

    compose_file_path = construct_path(config.get("compose_file_path"))

    container_compose_down(compose_file_path)
    delete_logs(log_path)
    container_compose_up(compose_file_path)
