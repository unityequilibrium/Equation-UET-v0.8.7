# 🏛️ UET Research Structure

*Clean, organized structure - Updated 2026-01-01*

---

## 📁 Current Structure

```
research_uet/
│
├── 📄 README.md                    # Project intro
├── 📄 MASTER_STRUCTURE.md          # This guide
├── 📄 DATA_MAP.md                  # Data locations
│
├── lab/                            # 🔬 All tests & code
│   ├── 01_particle_physics/        # QCD, Weak, Neutrino
│   ├── 02_astrophysics/            # Galaxies, Black Holes
│   ├── 03_condensed_matter/        # Casimir, Josephson
│   ├── 04_quantum/                 # Bell tests
│   ├── 05_unified_theory/          # Muon g-2, Action
│   ├── 06_complex_systems/         # Brain, Economy
│   └── 07_utilities/               # Tests, Analysis
│
├── data/                           # 📦 All data & references
│   ├── 01_particle/                # Particle Physics Data
│   ├── 02_astro/                   # Astrophysics Data
│   ├── 03_condensed/               # Condensed Matter Data
│   ├── 07_references/              # Reference Papers/PDFs
│   └── references/                 # Raw sources/JSONs
│
├── theory/                         # 📝 Papers & docs
│   ├── UET_FULL_PAPER.md           # The Main Paper
│   ├── UET_2026_THEORY.md          # 2026 update
│   └── UET_MASTER_EQUATION.md      # Mathematical Proofs
│
├── outputs/                        # 📊 Validation results
│   ├── 01_particle/
│   ├── 02_astro/
│   └── MASTER_SUMMARY.md           # Final Results
│
└── engine/                         # ⚙️ UET core code
```

---

## ✅ Migration Status (2026)

| Old Folder | New Folder | Status |
|:---|:---|:---|
| `data_vault/` | `data/` | ✅ Migrated |
| `evidence/` | `data/02_astro/` | ✅ Migrated |
| `validation_outputs/` | `outputs/` | ✅ Migrated |
| `docs/` | `theory/` | ✅ Merged |

---

## 🎯 Quick Reference

| What | Where |
|:---|:---|
| Tests | `lab/[category]/` |
| Data | `lab/[cat]/[mod]/data/` or `data/` |
| Papers | `theory/papers/` |
| Results | `outputs/` |
| Plots | `outputs/*.png` |
| PDFs | `data/references/papers_pdf/` |

---

*Structure v2.0 | Cleaned 2026-01-01*
