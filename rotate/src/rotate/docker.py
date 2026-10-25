import subprocess


def container_get_id_by_name(name: str):
    output = subprocess.run(
        ["docker", "ps", "--format", '"{{.Id}} {{.Name}}"'],
        check=True,
        capture_output=True,
        text=True,
    )

    for line in output.stdout.splitlines():
        if name in line:
            return line.split(" ")[0]
    raise ValueError("No container found matching given name")


def container_diff(id: str) -> dict[str, list[str]]:
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


def container_export_by_id(id: str, output_dir: str):
    subprocess.run(["docker", "export", "-o", output_dir, id], check=True)
