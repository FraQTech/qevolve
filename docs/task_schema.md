# QEVOLVE-Bench Task Schema

Each QEVOLVE-Bench task is a small executable project representing a quantum software evolution problem.

A task is stored as a directory under:

```text
benchmarks/controlled/seed_projects/

Each task directory should contain:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   task.yamlrequirements.txtbenchmark_notes.mdfailing_output.txtpassing_output.txtsrc/tests/   `

Required files
--------------

### task.yaml

The task metadata file. It identifies the task, ecosystem, category, dependencies, checks, and acceptance criteria.

Typical fields:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   id: qevolve_qiskit_ctrl_0004title: Controlled Qiskit QASM export migrationecosystem: qiskitcategory: circuit_export_migrationsource: controlledrepo:  url: "."  commit_before: ""  commit_after: ""env:  kind: venv  python: "3.11"  pip:    - "qiskit==2.3.1"    - "pytest==8.3.5"checks:  - name: tests    cmd: "pytest -q"    timeout_sec: 300acceptance:  must_pass:    - tests  require_initial_failure: truebudget:  max_iterations: 4  max_minutes: 10   `

### requirements.txt

Pinned Python dependencies for reproducing the passing task state.

Examples:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   qiskit==2.3.1pytest==8.3.5   `

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pennylane==0.44.1pytest==8.3.5   `

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cirq==1.6.1pytest==8.3.5   `

### benchmark\_notes.md

A short human-readable explanation of:

*   the ecosystem,
    
*   the task category,
    
*   the failure signal,
    
*   the intended repair,
    
*   the acceptance check,
    
*   and any caveats.
    

### failing\_output.txt

Captured output from the task before repair. This file records the intended failure signal, such as an import error, removed API error, attribute error, or changed execution interface.

### passing\_output.txt

Captured output from the task after repair. This file records the passing acceptance check.

### src/

The source code under repair.

### tests/

The executable acceptance tests.

Admission criteria for controlled tasks
---------------------------------------

A controlled task should satisfy the following:

1.  The failure is caused by a plausible quantum SDK evolution issue.
    
2.  The task has a reproducible failing state.
    
3.  The task has a reproducible passing state.
    
4.  The acceptance check is deterministic.
    
5.  The task is simulator-only and does not require external cloud services.
    
6.  The dependencies are pinned.
    
7.  The task runs in a bounded time budget.
    
8.  The repair is maintenance-level rather than a complete rewrite.
    

Current task families
---------------------

The current release includes tasks from these migration families:

*   removed execution APIs,
    
*   QuantumInstance removal,
    
*   parameter binding migration,
    
*   circuit export migration,
    
*   backend/provider namespace drift,
    
*   fake backend or testing helper migration,
    
*   import path rename,
    
*   PennyLane OpenQASM helper migration,
    
*   PennyLane legacy device-name removal,
    
*   PennyLane execute keyword removal,
    
*   PennyLane operator/helper migration,
    
*   Cirq deprecated base-class migration,
    
*   Cirq deprecated helper/protocol migration.
    

Adding a new task
-----------------

To add a new task:

1.  Create a new directory under benchmarks/controlled/seed\_projects/.
    
2.  Add src/ and tests/.
    
3.  Pin dependencies in requirements.txt.
    
4.  Run the failing state and save output as failing\_output.txt.
    
5.  Apply the repair.
    
6.  Run the passing state and save output as passing\_output.txt.
    
7.  Write task.yaml.
    
8.  Write benchmark\_notes.md.
    
9.  Add the task to benchmarks/controlled/manifest.csv.
    
10.  Run:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python scripts\smoke_check.py   `

The sanity checker should pass before committing.