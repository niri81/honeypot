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
    container_name = config.get("container_name")
    if not container_name:
        raise ValueError("Container name not defined in config")

    container_id = container_get_id_by_name(container_name)
    log_path = construct_path(config.get("log_path"))

    diff = container_diff_against_baseline(container_id, config.get("baseline"))
    logger.info(f"Diff between container and baseline is: {json.dumps(diff)}")
    if diff.values():
        notifier = Notifier(config.get("notifiers"))
        notifier.notify("Diff Detected", json.dumps(diff))

        container_export_by_id(
            container_id,
            output_dir=log_path / "container_fs",
        )

        save_logs_and_fs(log_path, construct_path(config.get("output_path")))

    compose_file_path = construct_path(config.get("compose_file_path"))

    container_compose_down(compose_file_path)
    delete_logs(log_path)
    container_compose_up(compose_file_path)
