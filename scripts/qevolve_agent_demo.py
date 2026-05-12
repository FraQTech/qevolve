from pathlib import Path
import argparse
import csv
import json
import re
from datetime import datetime


ROOT = Path(__file__).resolve().parents[1]


REPAIR_HINTS = {
    "removed_execute_api": [
        "Replace removed direct execution API usage with a modern backend/transpile/run workflow.",
        "Prefer explicit simulator/backend construction and pytest-verifiable output.",
    ],
    "quantuminstance_removal": [
        "Remove QuantumInstance usage.",
        "Use transpile(circuit, backend) and backend.run(transpiled_circuit, shots=...).",
    ],
    "parameter_binding_migration": [
        "Replace removed bind_parameters usage.",
        "Use assign_parameters with an explicit parameter mapping.",
    ],
    "circuit_export_migration": [
        "Replace removed QuantumCircuit.qasm() usage.",
        "Use the supported qiskit.qasm2.dumps(circuit) export helper.",
    ],
    "backend_provider_namespace_drift": [
        "Update backend/provider import paths.",
        "Use supported fake-provider or simulator interfaces under the pinned Qiskit version.",
    ],
    "testing_helper_migration": [
        "Replace removed testing/helper import paths.",
        "Use the modern helper or public testing utility exposed by the SDK.",
    ],
    "import_path_rename": [
        "Update renamed import paths.",
        "Prefer stable public SDK namespaces over private modules.",
    ],
    "openqasm_export_helper_migration": [
        "Replace removed or changed OpenQASM helper.",
        "Use the currently supported PennyLane OpenQASM export path.",
    ],
    "legacy_device_name_removal": [
        "Replace legacy PennyLane device names such as default.qubit.autograd or default.qubit.legacy.",
        "Use qml.device('default.qubit', wires=...).",
    ],
    "execution_keyword_removal": [
        "Remove obsolete execution keywords.",
        "Call qml.execute with the supported current signature.",
    ],
    "operator_helper_migration": [
        "Replace removed operator helper APIs.",
        "Use qml.simplify(op) or the modern public helper.",
    ],
    "deprecated_base_class_migration": [
        "Replace deprecated Cirq base classes.",
        "Subclass cirq.Gate and implement protocol methods such as _num_qubits_ and _unitary_.",
    ],
    "deprecated_helper_protocol_migration": [
        "Replace deprecated Cirq helper/protocol APIs.",
        "Use the current transformer/helper API and validate equivalence up to global phase when appropriate.",
    ],
}


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def extract_yaml_value(text: str, key: str) -> str:
    pattern = rf"^{re.escape(key)}:\s*[\"']?([^\"'\n]+)[\"']?\s*$"
    match = re.search(pattern, text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def summarize_failure(failing_output: str) -> str:
    signals = [
        "ModuleNotFoundError",
        "ImportError",
        "AttributeError",
        "TypeError",
        "QiskitError",
        "DeviceError",
        "ValueError",
        "AssertionError",
    ]

    lines = [line.strip() for line in failing_output.splitlines() if line.strip()]

    for signal in signals:
        for line in lines:
            if signal in line:
                return line

    for line in reversed(lines[-20:]):
        if "Error" in line or "FAILED" in line or "failed" in line:
            return line

    return "No concise failure signal detected; inspect failing_output.txt."


def build_repair_proposal(task_dir: Path) -> dict:
    task_yaml = read_text(task_dir / "task.yaml")
    notes = read_text(task_dir / "benchmark_notes.md")
    failing_output = read_text(task_dir / "failing_output.txt")

    task_id = extract_yaml_value(task_yaml, "id") or task_dir.name
    title = extract_yaml_value(task_yaml, "title")
    ecosystem = extract_yaml_value(task_yaml, "ecosystem")
    category = extract_yaml_value(task_yaml, "category")

    hints = REPAIR_HINTS.get(
        category,
        [
            "Inspect the failure signal and benchmark notes.",
            "Apply a minimal SDK migration that preserves the tested behavior.",
        ],
    )

    proposal = {
        "tool": "QEVOLVE-Agent prototype",
        "generated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "task_id": task_id,
        "title": title,
        "ecosystem": ecosystem,
        "category": category,
        "task_dir": str(task_dir.relative_to(ROOT)) if task_dir.is_relative_to(ROOT) else str(task_dir),
        "observed_failure_signal": summarize_failure(failing_output),
        "repair_plan": [
            "Read task metadata and benchmark notes.",
            "Identify the SDK-evolution failure category.",
            "Generate a minimal migration-oriented repair plan.",
            "Preserve existing tests and public behavior.",
            "Run the task acceptance check after applying the patch.",
        ],
        "category_specific_hints": hints,
        "evidence_files": [
            "task.yaml",
            "benchmark_notes.md",
            "failing_output.txt",
            "passing_output.txt",
            "requirements.txt",
        ],
        "prototype_scope": (
            "This prototype emits structured repair proposals for QEVOLVE-Bench tasks. "
            "It does not claim validated autonomous repair performance."
        ),
        "notes_excerpt": notes[:1200],
    }

    return proposal


def write_proposal(task_dir: Path, proposal: dict) -> Path:
    out_dir = ROOT / "outputs" / "agent_demo"
    out_dir.mkdir(parents=True, exist_ok=True)

    task_id = proposal["task_id"]
    out_path = out_dir / f"{task_id}_proposal.json"
    out_path.write_text(json.dumps(proposal, indent=2), encoding="utf-8")
    return out_path


def run_one(task_dir: Path) -> Path:
    if not task_dir.exists():
        raise FileNotFoundError(f"Task directory not found: {task_dir}")

    proposal = build_repair_proposal(task_dir)
    out_path = write_proposal(task_dir, proposal)

    print(f"[OK] Generated proposal for {proposal['task_id']}")
    print(f"[OK] Ecosystem: {proposal['ecosystem']}")
    print(f"[OK] Category: {proposal['category']}")
    print(f"[OK] Failure: {proposal['observed_failure_signal']}")
    print(f"[OK] Wrote: {out_path.relative_to(ROOT)}")

    return out_path


def run_manifest(manifest: Path) -> None:
    rows = list(csv.DictReader(manifest.open(newline="", encoding="utf-8")))
    for row in rows:
        task_dir = ROOT / row["task_dir"]
        run_one(task_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description="QEVOLVE-Agent prototype repair planner")
    parser.add_argument("--task-dir", help="Path to one QEVOLVE-Bench task directory")
    parser.add_argument("--manifest", help="Path to manifest.csv; generates proposals for all tasks")
    args = parser.parse_args()

    if not args.task_dir and not args.manifest:
        parser.error("Provide --task-dir or --manifest")

    if args.task_dir:
        run_one((ROOT / args.task_dir).resolve())

    if args.manifest:
        run_manifest((ROOT / args.manifest).resolve())


if __name__ == "__main__":
    main()