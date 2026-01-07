# UET Complete Data Map - All 14 Solutions

## 🎯 Overview

ทุก Solution ต้องมี:
1. **Real Data** - ข้อมูลจริงจาก sources ที่เชื่อถือได้
2. **References** - Papers + DOIs
3. **Test Scripts** - Validate UET predictions
4. **Results** - Comparison with standard physics

---

## 0.1 Galaxy Rotation Problem

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| galaxy_rotation_175 | Rotation Curves | **SPARC** (Lelli 2016) | `2016AJ....152..157L` |
| compact_galaxies | High Surface Brightness | SPARC subset | Same |
| dwarf_galaxies | Low Surface Brightness | **LITTLE THINGS** (Hunter 2012) | `2012AJ....144..134H` |
| galaxy_clusters | Virial Mass | Coma, Bullet Cluster | Multiple |

### Data Files Needed:
- [ ] `sparc_175_rotcurves.csv` - All 175 SPARC galaxies
- [ ] `little_things_26.csv` - 26 dwarf irregulars
- [ ] `cluster_mass.json` - Coma, Bullet, Abell

---

## 0.2 Black Hole Physics

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| black_holes_eht | Shadow Images | **EHT M87*** (2019) | `2019ApJ...875L...1E` |
| black_hole_saturation | No Singularity | Bekenstein Bound | Theory |
| ligo_waves | Gravitational Waves | **LIGO O3** (2021) | `2021PhRvX..11b1053A` |

### Data Files Needed:
- [ ] `eht_m87_shadow.json` - θ = 42±3 μas
- [ ] `eht_sgra_shadow.json` - θ = 51.8±2.3 μas
- [ ] `gwtc3_catalog.csv` - LIGO/Virgo events

---

## 0.3 Cosmology Hubble Tension

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| hubble_tension | H₀ Disagreement | **Planck 2018** + **SH0ES** | Multiple |
| bao | Baryon Acoustic | **BOSS/eBOSS** | `2017MNRAS.470.2617A` |
| cmb | CMB Power Spectrum | **Planck 2018** | `2020A&A...641A...6P` |

### Data Files Needed:
- [ ] `planck_2018_params.json` - H₀ = 67.4 ± 0.5
- [ ] `shoes_h0.json` - H₀ = 73.0 ± 1.0
- [ ] `boss_bao.csv` - BAO measurements

---

## 0.4 Superconductivity & Superfluids

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| superconductivity_tc | Critical Temp | **McMillan 1968** | `1968PhRv..167..331M` |
| superfluids_he4 | λ-transition | Donnelly 1998 | Standard |
| plasma | Fusion Confinement | **JET 2024** | Recent |

### Data Files Needed:
- [ ] `mcmillan_tc_30.json` - Tc for 30+ elements
- [ ] `he4_lambda.json` - λ-transition data
- [ ] `jet_fusion_2024.json` - JET record

---

## 0.5 Nuclear Binding & Hadrons

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| nuclear_binding_250 | Binding Energy | **AME2020** | `2021ChPhC..45c0003W` |
| proton_radius | Charge Radius | **CODATA 2018** | Standard |
| quark_masses | Quark Hierarchy | **PDG 2024** | `pdg.lbl.gov` |

### Data Files Needed:
- [ ] `ame2020_binding.csv` - 250+ isotopes
- [ ] `proton_radius.json` - 0.8414 fm
- [ ] `pdg_quarks_2024.json` - u,d,s,c,b,t masses

---

## 0.6 Electroweak Physics

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| wz_ratio | W/Z Mass | **PDG 2024** | `pdg.lbl.gov` |
| higgs_mass | 125.25 GeV | **LHC 2024** | ATLAS/CMS |
| sin2_theta_w | Weinberg Angle | **PDG 2024** | Standard |

### Data Files Needed:
- [ ] `pdg_electroweak_2024.json` - M_W, M_Z, θ_W
- [ ] `lhc_higgs_2024.json` - M_H = 125.25 GeV

---

## 0.7 Neutrino Physics

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| pmns_mixing | Mixing Angles | **T2K, NOvA, Daya Bay** | Multiple |
| neutrino_mass | Mass Limit | **KATRIN 2022** | `2022NatPh..18..160A` |
| beta_decay | ft-values | **Hardy 2020** | `2020PhRvC.102d5501H` |

### Data Files Needed:
- [ ] `pmns_2024.json` - θ₁₂, θ₂₃, θ₁₃
- [ ] `katrin_mass.json` - m < 0.8 eV
- [ ] `hardy_ftvalues.json` - Superallowed β

---

## 0.8 Muon g-2 Anomaly

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| muon_g2 | Magnetic Moment | **Fermilab 2023** | `2023PhRvL.131p1802A` |

### Data Files Needed:
- [ ] `fermilab_g2_2023.json` - Δa_μ = 2.5×10⁻⁹

---

## 0.9 Quantum Nonlocality

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| bell_inequality | CHSH Test | **Hensen 2015** (Loophole-free) | `2015Natur.526..682H` |
| double_slit | Interference | Textbook | Standard |

### Data Files Needed:
- [ ] `bell_test_2015.json` - S = 2.42±0.20

---

## 0.10 Fluid Dynamics & Chaos

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| poiseuille | Pipe Flow | **NIST** | Standard |
| turbulence | Re Transition | Standard | Standard |
| three_body | Chaos | Numerical | Standard |
| brownian | MSD | **Perrin 1908** | Historical |

### Data Files Needed:
- [ ] `nist_viscosity.json` - Fluid properties
- [ ] `perrin_msd.json` - Einstein relation

---

## 0.11 Phase Transitions

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| phase_separation | Spinodal | Al-Zn (Rundman 1967) | Historical |
| bec | Bose-Einstein | Cornell/Wieman 1995 | Nobel 2001 |

### Data Files Needed:
- [ ] `alzn_spinodal.json` - Phase separation
- [ ] `bec_1995.json` - Critical temp

---

## 0.12 Vacuum Energy & Casimir

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| casimir_effect | Vacuum Force | **Mohideen 1998** | `1998PhRvL..81.4549M` |

### Data Files Needed:
- [ ] `casimir_1998.json` - Force vs distance

---

## 0.13 Thermodynamic Bridge (MOST IMPORTANT!)

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| landauer | Info-Energy | **Bérut 2012** | `2012Natur.483..187B` |
| bekenstein | Entropy Bound | Bekenstein 1981 | `1981PhRvD..23..287B` |
| jacobson | Thermo → GR | Jacobson 1995 | `1995PhRvL..75.1260J` |

### Data Files Needed:
- [ ] `berut_2012.json` - Landauer limit verified
- [ ] `bekenstein_bound.json` - S ≤ 2πRE/ℏc

---

## 0.14 Complex Systems

### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| economy | Markets | **Yahoo Finance** | API |
| climate | CO2-Temp | **NOAA/NASA** | Public |
| biology_hrv | Heart Rate | **PhysioNet** | Public |
| inequality | Gini | **World Bank** | Public |

### Data Files Needed:
- [ ] `sp500_volatility.csv` - Stock data
- [ ] `noaa_co2_temp.csv` - Climate
- [ ] `physionet_hrv.csv` - HRV samples
- [ ] `worldbank_gini.csv` - Gini coefficients

---

## 📊 Summary

| Solution | Sections | Data Files | Priority |
|:---------|:--------:|:----------:|:--------:|
| 0.1 Galaxy | 4 | 3 | ⭐⭐⭐ |
| 0.2 Black Hole | 3 | 3 | ⭐⭐⭐ |
| 0.3 Cosmology | 3 | 3 | ⭐⭐⭐ |
| 0.4 SC/SF | 3 | 3 | ⭐⭐ |
| 0.5 Nuclear | 3 | 3 | ⭐⭐⭐ |
| 0.6 EW | 3 | 2 | ⭐⭐ |
| 0.7 Neutrino | 3 | 3 | ⭐⭐ |
| 0.8 g-2 | 1 | 1 | ⭐⭐ |
| 0.9 Quantum | 2 | 1 | ⭐ |
| 0.10 Fluid | 4 | 2 | ⭐ |
| 0.11 Phase | 2 | 2 | ⭐ |
| 0.12 Casimir | 1 | 1 | ⭐ |
| 0.13 Thermo | 3 | 2 | ⭐⭐⭐⭐⭐ |
| 0.14 Complex | 4 | 4 | ⭐ |
| **TOTAL** | **39** | **33** | |

---

## 🔗 Data Download Sources

### Physics Data:
- **PDG**: https://pdg.lbl.gov/
- **NIST**: https://www.nist.gov/
- **AME2020**: https://www-nds.iaea.org/amdc/

### Astro Data:
- **SPARC**: http://astroweb.cwru.edu/SPARC/
- **EHT**: https://eventhorizontelescope.org/
- **LIGO**: https://gwosc.org/

### Public APIs:
- **Yahoo Finance**: yfinance Python package
- **NOAA**: https://www.ncei.noaa.gov/
- **World Bank**: https://data.worldbank.org/

---

## 0.15 Cluster Dynamics
### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| virial_mass | Missing Baryons | **Coma Cluster** | Standard |
| recoil_pooling | Halo Formation | Simulation | UET Specific |

### Data Files Needed:
- [ ] `coma_cluster_data.json` - Velocity dispersion

---

## 0.16 Heavy Nuclei (Island of Stability)
### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| fission_barrier | Stability Limit | **AME2020** | Same as 0.5 |
| island_stability | Z=114, N=184 | Theory/Models | Nuclear Models |

### Data Files Needed:
- [ ] `ame2020_heavy.csv` - Transuranic masses

---

## 0.17 Mass Generation (Higgs Alternative)
### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| koide_relation | Lepton Masses | **PDG 2024** | $m_e, m_\mu, m_\tau$ |
| mass_gap | YM Millenium | Theory | Mathematical |

### Data Files Needed:
- [ ] `lepton_masses.json` - Precise values

---

## 0.18 Neutrino Mixing (Full Matrix)
### Sections:
| Section | Phenomenon | Real Data Source | DOI/Link |
|:--------|:-----------|:-----------------|:---------|
| pmns_full | CP Violation | **T2K / NOvA** | `2020Natur.580..339A` |
| geometric_phase | Berry Phase | Theory | UET derivation |

### Data Files Needed:
- [ ] `pmns_matrix.json` - Complex phases

---
**End of Map (v1.5 Verified)**
