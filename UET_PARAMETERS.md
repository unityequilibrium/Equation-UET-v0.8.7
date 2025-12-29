# UET Parameter Reference

This document defines the key parameters used in the UET (Universal Evolution Thermodynamics) simulation harness.

## Core Parameters

### `beta` (Inverse Temperature)
- **Symbol**: $\beta$
- **Description**: Controls the noise level in the Langevin dynamics. Higher $\beta$ means lower noise (temperature).
- **Role**: Determines the stochasticity of the evolution.
- **Physical Analogy**: $1/(k_B T)$.

### `s` / `s_tilt` (Tilt)
- **Symbol**: $s$
- **Description**: A linear tilt applied to the potential landscape.
- **Role**: Biases the system towards one state or another (symmetry breaking).
- **Variants**:
  - `s_tilt`: The net difference in tilt between Conscience (C) and Instinct (I) fields. Differential tilt ($s_C - s_I$) is the driver of phase transitions in the map.
  - `sC`, `sI`: Individual tilts applied to C and I potentials.

### `kappa` (Coupling)
- **Symbol**: $\kappa$
- **Description**: Strength of the coupling term in the potential.
- **Role**: Interactions between fields.

### `delta` (Barrier/Shape)
- **Symbol**: $\delta$ / $\Lambda$
- **Description**: Controls the height of the potential barrier or the shape of the quartic potential ($\Lambda$ in some contexts).
- **Role**: Determines the stability of states and the difficulty of transitions.

### `asym` (Asymmetry)
- **Symbol**: $A_{sym}$
- **Description**: Introduces intrinsic asymmetry into the potential function itself (distinct from linear tilt).

## Coupling & Timescales

### `k_ratio` (Coupling Ratio)
- **Symbol**: $k_C / k_I$
- **Description**: The ratio of coupling constants for C and I fields.
- **Role**: Determines which field dominates the interaction strength.

### `MC`, `MI` (Mass/Inertia)
- **Symbol**: $M_C$, $M_I$
- **Description**: "Mass" or inertia terms in the dynamical equations.
- **Role**: Effectively sets the **timescale** of evolution for each field.
- **Key Insight**: $M$ behaves as a timescale parameter. Higher $M$ = slower relaxation ($t_{relax}$).

### `Mr` / `Mr_effective` (Mass Ratio)
- **Symbol**: $M_r = M_I / M_C$
- **Description**: The ratio of timescales between Instinct and Conscience.
- **Role**: Controls the relative speed of dynamics. Does **not** affect the equilibrium state use (OmegaT), only the transient path (trajectory).

## Simulation & Output Metrics

- **`OmegaT`**: Final value of the order parameter (equilibrium state).
- **`t_relax`**: Time taken to relax to equilibrium.
- **`bias_CI`**: Difference between mean C and mean I values ($\bar{C} - \bar{I}$). Used to detect symmetry breaking.
- **`grade_bias`**: Classification of the run results:
  - `SYM`: Symmetric (no bias).
  - `BIAS_C`: Biased towards Conscience (positive).
  - `BIAS_I`: Biased towards Instinct (negative).
