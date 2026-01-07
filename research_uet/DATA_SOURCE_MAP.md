# UET Data Source Master Map
**Purpose**: To verify that UET is testing against **Real Nature**, not just self-generated loops.

## Type A: Mass External Datasets (The Heavy Lifters)
These tests read large tables of real-world observations.
1.  **0.1 Galaxy Rotation**:
    *   **Source**: `SPARC` Database (Lelli et al., 2016).
    *   **Content**: 175 Galaxy Rotation Curves (CSV).
    *   **Reality**: 100% Real Observation.
2.  **0.5 Nuclear Binding**:
    *   **Source**: `AME2020` (Atomic Mass Evaluation).
    *   **Content**: 3,000+ Isotope Masses.
    *   **Reality**: 100% Real NIST Data.
3.  **0.16 Heavy Nuclei**:
    *   **Source**: `AME2020` (Subset: Uranium/Plutonium).
    *   **Reality**: Shared with 0.5 (Same Source, Different Domain).

## Type B: Precision Empirical Constants (The Benchmarks)
These tests compare UET formulas against a specific, highly accurate measured value.
4.  **0.2 Black Hole**:
    *   **Source**: EHT Collaboration (M87*, Sgr A*).
    *   **Data**: Mass/Shadow Diameter Ratios.
5.  **0.3 Hubble**:
    *   **Source**: Planck 2018 vs SH0ES 2022.
    *   **Data**: $H_0$ values ($67.4$ vs $73.0$).
6.  **0.4 Superconductivity**:
    *   **Source**: Experiment records (Hg, Pb, YBCO).
    *   **Data**: Critical Temperatures ($T_c$).
7.  **0.6 Electroweak**:
    *   **Source**: Particle Data Group (PDG).
    *   **Data**: W/Z Boson Masses, Weinberg Angle.
8.  **0.7 Neutrino**:
    *   **Source**: Super-Kamiokande / NOvA.
    *   **Data**: $\Delta m^2$ and Mixing Angles.
9.  **0.8 Muon g-2**:
    *   **Source**: Fermilab E989.
    *   **Data**: Anomalous magnetic moment $a_\mu$.
10. **0.12 Casimir**:
    *   **Source**: Lamoreaux et al.
    *   **Data**: Force vs Distance curves.
11. **0.17 Mass Gen**:
    *   **Source**: PDG (Lepton Masses).
    *   **Data**: Koide Relation values ($e, \mu, \tau$).

## Type C: Mechanism Simulations (The Logic Checks)
These tests simulate a process to see if UET logic holds (Qualitative Match).
12. **0.9 Non-Locality**:
    *   **Method**: Simulating Bell Test Statistics.
    *   **Status**: Synthetic (Math Check), but matches Aspect Experiment results.
13. **0.10 Fluid/Chaos**:
    *   **Method**: Simulating Navier-Stokes + Recoil.
    *   **Status**: Synthetic (Mechanism Check).
14. **0.11 Phase Transitions**:
    *   **Method**: Simulating BEC condensation curve.
    *   **Status**: Synthetic (Curve Match).
15. **0.13 - 0.15 - 0.18**:
    *   Mostly theoretical extensions or deriving behavior from earlier constants.

## Verdict
*   **Is it all fake?** No. 11 out of 18 topics use **Hard Empirical Data**.
*   **Is it independent?** Yes. 0.1 (Galaxies) uses totally different data from 0.8 (Muons). It is not circular.
