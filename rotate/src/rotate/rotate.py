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

        falco_log_path = construct_path(config.get("falco_log_path"))

        diff = container_diff_against_baseline(
            container_id, container.get("baseline", "")
        )
        logger.info(f"Diff between container and baseline is: {json.dumps(diff)}")
        if any(diff.values()) or falco_log_path.exists():
            notifier = Notifier(config.get("notifiers"))
            notifier.notify(
                f"Diff Detected for Container {container_name}", json.dumps(diff)
            )

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
