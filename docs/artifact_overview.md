# QEVOLVE-Bench Artifact Overview

QEVOLVE-Bench is an executable benchmark for studying quantum software evolution across Qiskit, PennyLane, and Cirq.

The current release focuses on controlled SDK-migration tasks. Each task captures a small, reproducible breakage caused by quantum SDK API evolution, dependency drift, or interface removal. The benchmark is designed for researchers and tool builders studying automated program repair, dependency migration, LLM-based code repair, and quantum software maintenance.

## What the artifact contains

The artifact contains:

- 14 controlled benchmark tasks
- tasks spanning Qiskit, PennyLane, and Cirq
- pinned dependency requirements for each task
- failing and passing output logs
- deterministic simulator-only pytest checks
- task-level metadata in `task.yaml`
- benchmark notes explaining the failure signal and intended repair
- a manifest describing the task inventory
- smoke-test logs for one representative task per ecosystem
- a sanity-check script for validating the artifact structure

## Repository layout

```text
benchmarks/
  controlled/
    manifest.csv
    seed_projects/
      qevolve_qiskit_ctrl_0001/
      ...
      qevolve_pennylane_ctrl_0014/
docs/
  artifact_overview.md
  task_schema.md
outputs/
  smoke/
scripts/
  smoke_check.py


Benchmark task model
--------------------

Each task represents a small software project that has been migrated from a failing state to a passing state under a pinned newer SDK version. The task includes:

*   source code under src/
    
*   tests under tests/
    
*   dependency pins in requirements.txt
    
*   metadata in task.yaml
    
*   failure evidence in failing\_output.txt
    
*   passing evidence in passing\_output.txt
    
*   human-readable notes in benchmark\_notes.md
    

The current release includes only controlled tasks. Real-world repository tasks are planned as a future extension.

Current task inventory
----------------------

The current release contains 14 controlled tasks:

EcosystemCountQiskit7PennyLane5Cirq2

The task inventory is stored in:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   benchmarks/controlled/manifest.csv   `

Evidence of executability
-------------------------

The artifact includes representative smoke-test logs for one task per ecosystem:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   outputs/smoke/qiskit_ctrl_0004_smoke.txtoutputs/smoke/pennylane_ctrl_0009_smoke.txtoutputs/smoke/cirq_ctrl_0010_smoke.txt   `

These logs show that representative Qiskit, PennyLane, and Cirq tasks can be installed and run in isolated virtual environments using their pinned dependencies.

Intended use cases
------------------

QEVOLVE-Bench is intended to support:

1.  evaluation of automated repair systems on quantum SDK migration tasks,
    
2.  comparison of rule-based and LLM-based repair strategies,
    
3.  study of recurring quantum software maintenance patterns,
    
4.  development of new benchmark tasks for quantum software evolution,
    
5.  teaching and demonstration of API migration issues in quantum software.
    

Scope and limitations
---------------------

This release is intentionally scoped as an initial controlled benchmark. The current tasks are small and simulator-only by design. Passing a task means that the repaired project satisfies its executable acceptance checks; it does not imply full semantic equivalence for arbitrary quantum programs.

Future releases should add:

*   real repository tasks,
    
*   larger projects,
    
*   broader quantum SDK coverage,
    
*   richer repair-method evaluation,
    
*   and stronger semantic validation beyond executable tests.