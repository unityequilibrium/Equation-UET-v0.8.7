"""
Superfluid Data - Real Experimental Data
=========================================
Sources:
- Helium-4: Donnelly & Barenghi (1998)
- Helium-3: Leggett (1975)
- BEC: Cornell & Wieman (1995), Ketterle (1995)

Updated: 2026-01-03
"""

import numpy as np

# He-4 Superfluid Properties
HELIUM_4_SUPERFLUID = {
    "lambda_point_K": 2.1768,
    "lambda_point_error_K": 0.0001,
    "critical_velocity_cm_s": 45.0,
    "density_g_cm3": 0.145,
    "second_sound_velocity_m_s": 20.0,
    "source": "Donnelly & Barenghi 1998",
}

# He-3 Superfluid (A and B phases)
HELIUM_3_SUPERFLUID = {
    "Tc_mK_A": 2.49,
    "Tc_mK_B": 1.93,
    "type": "p-wave pairing",
    "source": "Leggett 1975 / Nobel 2003",
}

# BEC Experiments
BEC_DATA = [
    # (atom, Tc_nK, N_atoms, year, source)
    ("Rb-87", 170, 2e3, 1995, "Cornell/Wieman"),
    ("Na-23", 2000, 5e5, 1995, "Ketterle"),
    ("Li-7", 400, 1e5, 1997, "Hulet"),
    ("H", 50, 1e9, 1998, "Kleppner"),
]

# Critical Temperatures
CRITICAL_TEMPERATURES = {
    "He4_superfluid": 2.1768,  # K
    "He3_A": 0.00249,  # K (mK)
    "He3_B": 0.00193,  # K (mK)
}


def superfluid_fraction(T_K, Tc_K):
    """
    Calculate superfluid fraction rho_s/rho.

    Uses power law: rho_s/rho = 1 - (T/Tc)^alpha
    where alpha ~ 5.6 for He-4
    """
    if T_K >= Tc_K:
        return 0.0
    alpha = 5.6
    return 1.0 - (T_K / Tc_K) ** alpha


def bec_critical_temp_K(n_density, mass_kg):
    """
    BEC critical temperature for ideal gas.

    Tc = (2*pi*hbar^2 / m*k_B) * (n / zeta(3/2))^(2/3)
    """
    from scipy.constants import hbar, k as k_B, pi
    from scipy.special import zeta

    zeta_32 = zeta(1.5)
    Tc = (2 * pi * hbar**2 / (mass_kg * k_B)) * (n_density / zeta_32) ** (2 / 3)
    return Tc
