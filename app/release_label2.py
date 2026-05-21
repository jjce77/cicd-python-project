def build_release_label(branch: str, status: str) -> str:
    return f"{branch}:{status}"


def build_release_summary(branch: str, status: str, owner: str) -> str:
    return f"{owner}@{branch}:{status}"


def build_release_tag(branch: str, status: str, version: str) -> str:
    return f"{branch}-{status}-{version}"
