# QEVOLVE-Bench

QEVOLVE-Bench is an executable benchmark for quantum software evolution tasks across Qiskit, PennyLane, and Cirq.

The current release contains controlled SDK-migration tasks with pinned environments, failing and passing states, deterministic tests, and benchmark notes.

## Repository layout

- `benchmarks/controlled/manifest.csv` — task inventory
- `benchmarks/controlled/seed_projects/` — executable seed projects
- `docs/` — task schema and artifact documentation
- `scripts/` — helper scripts
- `outputs/` — example outputs and smoke-test logs

## Documentation

- [Artifact overview](docs/artifact_overview.md)
- [Task schema](docs/task_schema.md)
- [Repair harness design](docs/repair_harness_design.md)
- [Screencast script](docs/screencast_script.md)

## Current release

This release contains 14 controlled quantum software evolution tasks:

- 7 Qiskit tasks
- 5 PennyLane tasks
- 2 Cirq tasks

Each task is simulator-only and designed to capture a maintenance-level SDK migration.

## Quickstart: run one task

Example using the Qiskit OpenQASM export migration task:

```cmd
cd benchmarks\controlled\seed_projects\qevolve_qiskit_ctrl_0004
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
