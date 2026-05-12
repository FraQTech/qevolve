from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "benchmarks" / "controlled" / "manifest.csv"

REQUIRED_FILES = [
    "task.yaml",
    "benchmark_notes.md",
    "failing_output.txt",
    "passing_output.txt",
    "requirements.txt",
]

REQUIRED_DIRS = [
    "src",
    "tests",
]

# These directories may appear after local smoke tests, but must not be tracked.
IGNORED_RUNTIME_DIRS = {
    ".venv",
    ".pytest_cache",
    "__pycache__",
    ".git",
}


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    sys.exit(1)


def iter_non_runtime_paths(root: Path):
    """Walk a tree while skipping local generated runtime directories."""
    stack = [root]
    while stack:
        current = stack.pop()
        if current.name in IGNORED_RUNTIME_DIRS:
            continue
        yield current
        if current.is_dir():
            for child in current.iterdir():
                if child.name not in IGNORED_RUNTIME_DIRS:
                    stack.append(child)


def main() -> None:
    if not MANIFEST.exists():
        fail(f"Missing manifest: {MANIFEST}")

    rows = list(csv.DictReader(MANIFEST.open(newline="", encoding="utf-8")))

    if len(rows) != 14:
        fail(f"Expected 14 tasks in manifest, found {len(rows)}")

    seen_ids = set()

    for row in rows:
        task_id = row["id"]
        if task_id in seen_ids:
            fail(f"Duplicate task id in manifest: {task_id}")
        seen_ids.add(task_id)

        task_dir = ROOT / row["task_dir"]

        if not task_dir.exists():
            fail(f"{task_id}: missing task directory: {task_dir}")

        for name in REQUIRED_FILES:
            path = task_dir / name
            if not path.exists():
                fail(f"{task_id}: missing required file: {name}")

        for name in REQUIRED_DIRS:
            path = task_dir / name
            if not path.exists() or not path.is_dir():
                fail(f"{task_id}: missing required directory: {name}")

        # Walk the tree while ignoring local runtime artifacts.
        # This ensures the checker still works after users run pytest locally.
        for _ in iter_non_runtime_paths(task_dir):
            pass

    ecosystems = {}
    for row in rows:
        ecosystems[row["ecosystem"]] = ecosystems.get(row["ecosystem"], 0) + 1

    print("[OK] QEVOLVE-Bench artifact sanity check passed.")
    print(f"[OK] Tasks: {len(rows)}")
    print(f"[OK] Ecosystems: {ecosystems}")
    print(f"[OK] Manifest: {MANIFEST.relative_to(ROOT)}")
    print("[OK] Local runtime directories such as .venv and .pytest_cache are ignored.")


if __name__ == "__main__":
    main()