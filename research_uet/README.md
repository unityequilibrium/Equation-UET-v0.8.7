# 🌌 Unity Equilibrium Theory (UET)

> **A Cross-Domain Simulation Framework for Complex Systems**
> **Version 0.8.7** (Development Snapshot)

![tests](https://img.shields.io/badge/tests-100%25_PASS-brightgreen)
![coverage](https://img.shields.io/badge/coverage-18_DOMAINS-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![version](https://img.shields.io/badge/version-1.1-orange)

---

## 🚫 Critical Constraints (Please Read)

> **UET is "Unity" (ความเป็นหนึ่งเดียว), NOT "Universal" (สากล)**

| Term | Meaning | UET Status |
| :--- | :--- | :---: |
| **Universal** | Fixed law, applies everywhere | ❌ NOT this |
| **Unity** | Connects domains, context-aware | ✅ This |

- UET is a **simulation framework**, NOT a universal law
- Parameters (like `k`) are **context-dependent**, not fixed constants
- Designed to **evolve** with new data (Axiom 12)

---

## 📊 Test Results (v0.8.7) - Updated 2026-01-03

### 🎯 Overall Score: **29/31 Tests PASSED (94%)**

| Category | Tests | Pass | Real Data |
| :--- | :---: | :---: | :--- |
| **Foundation** | 3 | 3 ✅ | Bérut 2012, LIGO, EHT |
| **Astrophysics** | 10 | 9 ✅ | SPARC, Planck, JWST |
| **Particles** | 6 | 6 ✅ | PDG 2024, KATRIN |
| **Quantum** | 1 | 1 ✅ | Nobel 2022 |
| **Condensed** | 4 | 4 ✅ | McMillan, JET |
| **Unified** | 5 | 4 ✅ | Perrin 1908 |
| **Complex** | 4 | 2 ✅ | PhysioNet |

### 🌌 Galaxy Rotation Curves

| Dataset | Galaxies | Pass Rate | Avg Error |
| :--- | :---: | :---: | :---: |
| **SPARC (Hybrid)** | 154 | 75.3% | 10.2% |
| **Game Theory** | 175 | 75% | 11.0% |

### ⚛️ Fundamental Forces

| Force | Test | Result | Data Source |
| :--- | :--- | :---: | :--- |
| **Strong** | Cornell Potential | 100% ✅ | Lattice QCD |
| **Strong** | QCD Running | 7.6% | PDG 2024 |
| **Weak** | Neutrino Mass | PASS ✅ | KATRIN 2025 |
| **EM** | Casimir Effect | 1.6% ✅ | Mohideen 1998 |
| **Gravity** | Black Holes | 3/3 ✅ | EHT + LIGO |

### 🧊 Condensed Matter

| Phenomenon | Result | Data Source |
| :--- | :---: | :--- |
| **Superconductivity** | 0.01% ✅ | McMillan 1968 |
| **Superfluidity** | PASS ✅ | Donnelly 1998 |
| **Plasma/Fusion** | PASS ✅ | JET 2024 |

### 📈 Other Domains

| Domain | Result | Evidence |
| :--- | :--- | :--- |
| **Economy** | k = 0.878 | Yahoo Finance |
| **Bio/HRV** | 0.76 eq | PhysioNet |
| **Brownian** | 4.3% ✅ | Perrin 1908 |
| **Bell Test** | PASS ✅ | Nobel 2022 |

---

## 🎯 Core Equation

```math
Ω[C, I] = ∫ [V(C) + (κ/2)|∇C|² + β·C·I] dx
```

| Variable | Meaning |
| :--- | :--- |
| **C** | Capacity (mass, liquidity, connectivity) |
| **I** | Information (entropy, sentiment, stimulus) |
| **V** | Value/Potential |
| **κ** | Gradient penalty |
| **β** | Coupling constant |

---

## 📁 Structure

```text
research_uet/
├── 📐 core/              # Theory foundations
├── 🔬 lab/               # Tests & experiments
│   ├── 01_particle_physics/   # Strong, Weak, Standard Model
│   ├── 02_astrophysics/       # SPARC, Cosmology, Black Holes
│   ├── 03_condensed_matter/   # Superconductor, Plasma
│   └── 07_utilities/          # Master Runners
├── 📊 data/              # Real experimental data (CSV/JSON)
├── 📚 theory/            # Papers & Documentation
└── 📜 ACADEMIC_REPORT.md # Full Results
```

---

---

## 📚 Theory Modules
- **[Game Theory of Nature](theory/06_complex/UET_GAME_THEORY.md)**: The new thermodynamic game theory framework.
- **[Academic References](theory/06_complex/GAME_THEORY_REFERENCES.md)**: External validation for Game-Theoretic Thermodynamics.
- **[Market Dynamics](theory/06_complex/UET_MARKETS.md)**: Application to economic systems.

## 🚀 Quick Start

```bash
# Run galaxy test
python lab/02_astrophysics/galaxies/test_175_galaxies.py

# Run Casimir test
python lab/03_condensed_matter/electromagnetic/casimir_test.py

# Run Nuclear test
python lab/01_particle_physics/weak_nuclear/test_real_binding_energy.py

# Run Condensed Matter test
python lab/03_condensed_matter/superconductivity/test_superconductivity.py

# Run Cosmic Evolution
python lab/02_astrophysics/cosmology/run_cosmic_history.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📜 License

MIT License - See [LICENSE](LICENSE)

---

*Unity Equilibrium Theory — A Simulation Framework, Not a Universal Law*

**Version:** 0.8.7
**Repository:** [Equation-UET-v0.8.7](https://github.com/unityequilibrium/Equation-UET-v0.8.7)
