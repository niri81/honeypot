import subprocess
from pathlib import Path


def container_get_id_by_name(name: str):
    output = subprocess.run(
        ["docker", "ps", "--format", '"{{.ID}} {{.Name}}"'],
        check=True,
        capture_output=True,
        text=True,
    )

    for line in output.stdout.splitlines():
        if name in line:
            return line.split(" ")[0]
    raise ValueError("No container found matching given name")


def container_diff_against_baseline(id: str, baseline: str) -> dict[str, list[str]]:
    container_diff_dict = _container_diff(id)
    baseline_dict = _container_diff_output_to_dict(baseline)

    return _diff_change_set(container_diff_dict, baseline_dict)


def _diff_change_set(a, b):
    result = {"added": [], "modified": [], "removed": []}
    for key in result:
        items_a = set(a.get(key, []))
        items_b = set(b.get(key, []))

        result[key] = list(items_a - items_b)
    return result


def _container_diff(id: str) -> dict[str, list[str]]:
    output = subprocess.run(
        ["docker", "diff", id], check=True, capture_output=True, text=True
    )
    return _container_diff_output_to_dict(output.stdout)


def _container_diff_output_to_dict(output: str) -> dict[str, list[str]]:
    diff_dict: dict[str, list[str]] = {"added": [], "modified": [], "removed": []}

    for line in output.splitlines():
        if line.startswith("A"):
            diff_dict["added"].append(line[1:].strip())
        elif line.startswith("R"):
            diff_dict["removed"].append(line[1:].strip())
        elif line.startswith("M"):
            diff_dict["modified"].append(line[1:].strip())

    return diff_dict


def container_export_by_id(id: str, output_dir: Path):
    subprocess.run(["docker", "export", "-o", output_dir, id], check=True)


def container_compose_down(compose_file_path: Path):
    subprocess.run(["docker", "compose", "down"], check=True, cwd=compose_file_path)


def container_compose_up(compose_file_path: Path):
    subprocess.run(
        ["docker", "compose", "up", "-d", "--force-recreate"],
        check=True,
        cwd=compose_file_path,
    )
