"""
UET Universal Constants (Single Source of Truth)
================================================
Standardized physical constants based on CODATA 2024.
All UET scripts MUST import from here to ensure consistency.

Usage:
    from research_uet.theory.utility.universal_constants import G, c, h_bar
"""

import numpy as np

# ==========================================
# Fundamental Constants (SI Units)
# ==========================================
c = 2.99792458e8  # Speed of light in vacuum (m/s) (EXACT)
G = 6.67430e-11  # Newtonian constant of gravitation (m^3 kg^-1 s^-2)
h = 6.62607015e-34  # Planck constant (J s) (EXACT)
h_bar = h / (2 * np.pi)  # Reduced Planck constant (J s)
hbar = h_bar  # Alias
kB = 1.380649e-23  # Boltzmann constant (J/K) (EXACT)
e_charge = 1.60217663e-19  # Elementary charge (C) (EXACT)
mu_0 = 1.2566370614e-6  # Vacuum magnetic permeability (N/A^2)
epsilon_0 = 1 / (mu_0 * c**2)  # Vacuum electric permittivity (F/m)

# ==========================================
# Astrophysical Constants
# ==========================================
M_sun = 1.98847e30  # Solar mass (kg)
L_sun = 3.828e26  # Solar luminosity (W)
pc = 3.085677581e16  # Parsec (m)
kpc = 1e3 * pc
Mpc = 1e6 * pc
Mpc_to_m = Mpc  # Alias
Gyr = 3.15576e16  # Giga-year (s)
Year_to_sec = 3.15576e7  # Year in seconds
H0_planck = 67.4  # Hubble Constant (km/s/Mpc) (Planck 2018)
H0_shoes = 73.0  # Hubble Constant (km/s/Mpc) (SH0ES)
H0_uet = 70.2  # UET Theoretical Prediction

# ==========================================
# UET Theoretical Constants
# ==========================================
# Critical parameters derived from theory
k_ccbh = 2.8  # Cosmological Coupling Strength (Theory: 3.0, Fit: 2.8)
S_B_ratio = np.log(2)  # Landauer Limit Entropy Ratio (bits to nats)
