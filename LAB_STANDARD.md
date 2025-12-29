# UET Laboratory Standard (v1.0)
**The Blueprint for Paper-Centric Research**

## 🎯 Philosophy
Every folder in the UET Repository must be a "Self-Contained Scientific Unit." This ensures that if the repository grows to include 100 different fields, each remains testable and documented without breaking others.

## 📂 Directory Standard (Root)
- `src/`: **The Foundry.** Core PDE solvers, physical constants, and CLI tools. No experimental code allowed here.
- `research/`: **The Library.** Peer-reviewed or publication-ready work.
- `experiments/`: **The Workbench.** Ad-hoc sweeps, parameter testing, and raw trial data.
- `legacy_archive/`: **The Vault.** Non-destructive storage for historical scripts.

## 🔬 Research Folder Standard
Any folder inside `research/XX-domain/` MUST contain:
1. `paper.md / .tex`: The primary scientific output.
2. `harness/` or `01_data/`: The Python scripts used to generate the paper's results.
3. `README.md`: Instructions on how to reproduce the paper's claims.
4. `production_test_report.json`: (Generated) Proof of current validation status.

## 🚀 Multidisciplinary Workflow
To start a new research area (e.g., Economics):
1. Create `research/02-economics/`.
2. Link core UET engines via `from src.uet_core import ...`.
3. Draft the paper and code in parallel.
4. Add the validation script to the Master Harness if applicable.

---
**Standardized on 2025-12-28 by UET Research Team**
