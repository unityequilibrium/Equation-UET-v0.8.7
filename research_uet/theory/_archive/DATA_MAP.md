# 📊 UET Data Map

*Complete guide to all real data locations*

---

## ❓ The Problem

ข้อมูลกระจายอยู่ 2 ที่:
1. `data_vault/` - ข้อมูลเก่า (legacy)
2. `lab/*/data/` - ข้อมูลใหม่ (active)

---

## 🗂️ Data Locations Overview

```
research_uet/
│
├── data/                          # 📦 CENTERALIZED DATA
│   ├── particle_physics/          # PDG & Nuclear data
│   ├── astrophysics/              # SPARC & Black Holes
│   ├── condensed_matter/          # Casimir & Tc data
│   ├── cosmic/                    # Planck & Hubble data
│   └── references/                # Raw Papers & Sources
│
└── lab/                           # 🔬 EXPERIMENTAL CODE
    ├── 01_particle_physics/       # Strong/Weak Force Tests
    ├── 02_astrophysics/           # Galaxies/Cosmology Tests
    ├── 03_condensed_matter/       # Superconductor Tests
    └── ...
```

---

## 📋 Complete Data Location Table

| Data | Location | Source | Year | Status |
|:---|:---|:---|:---:|:---:|
| **QCD α_s** | `lab/01_particle_physics/qcd_fix/data/qcd_alpha_s_data.py` | PDG | 2024 | ✅ Active |
| **Hadron masses** | `lab/01_particle_physics/qcd_fix/data/hadron_mass_data.py` | PDG | 2024 | ✅ Active |
| **Muon g-2** | `lab/05_unified_theory/action_transformer/data/muon_g2_data.py` | Fermilab | **2025** | ✅ Active |
| **Casimir exp** | `lab/03_condensed_matter/electromagnetic/lamoreaux_1997_casimir.json` | Lamoreaux | 1997 | ✅ Active |
| **Weak force** | `data/particle_physics/weak_force_data.py` | NNDC | 2024 | ✅ Active |
| **SPARC** | `data/references/sparc_175.csv` | SPARC | 2016 | ✅ Active |

---

## ⭐ Primary Data (Use These!)

### 1. Particle Physics (PDG 2024)
```python
# Location: lab/01_particle_physics/
from research_uet.data.01_particle import weak_force_data
```

### 2. Muon g-2 (Fermilab 2025)
```python
# Location: lab/05_unified_theory/
from muon_g2_data import A_MU_EXPERIMENT
```

### 3. Casimir (Mohideen 1998)
```python
# Location: lab/03_condensed_matter/
import json
with open('mohideen_1998_casimir.json') as f:
    data = json.load(f)
```

---

## ⚠️ Legacy Note
The old `data_vault/` directory has been fully migrated to `data/`. Please use the new paths.

---

## 🔗 Data → Test Connections

| Data File | Test File | Error |
|:---|:---|:---:|
| `qcd_alpha_s_data.py` | `uet_qcd_bridge.py` | 7.6% |
| `hadron_mass_data.py` | `uet_hadron_model.py` | 3.9% |
| `muon_g2_data.py` | `test_muon_g2.py` | Core |
| `lamoreaux_1997.json` | `casimir_test.py` | 1.6% |
| `bell_test_data.py` | (future test) | - |
| `phase_separation_data.py` | `test_phase_separation.py` | 58% |

---

## 📥 Where to Add New Data

```
# New particle physics data
lab/01_particle_physics/[module]/data/

# New astrophysics data  
lab/02_astrophysics/[module]/data/

# Raw reference papers
data_vault/references/
```

---

## 🎯 Recommendation

**ใช้ข้อมูลใน `lab/` เป็นหลัก!**

- `lab/` = ข้อมูลใหม่, formatted, tested
- `data_vault/` = ข้อมูลเก่า, raw, backup

---

*Data Map v1.0 | 2026-01-01*
