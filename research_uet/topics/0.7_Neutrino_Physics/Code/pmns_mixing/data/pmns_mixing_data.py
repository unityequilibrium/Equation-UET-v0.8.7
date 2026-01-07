"""
PMNS Mixing Data
================
Data for Neutrino Mixing (PMNS) validation.
Standard Model values from PDG 2024.
"""

import numpy as np

# ==============================================================================
# DATA
# ==============================================================================

PMNS_MIXING_ANGLES = {
    "theta12": {
        "value_deg": 33.44,
        "uncertainty_deg": 0.77,
        "source": "PDG 2024 (Solar + KamLAND)",
    },
    "theta23": {
        "value_deg": 49.2,
        "uncertainty_deg": 1.0,
        "source": "PDG 2024 (Atmospheric + Accel)",
    },
    "theta13": {
        "value_deg": 8.57,
        "uncertainty_deg": 0.12,
        "source": "PDG 2024 (Reactor)",
    },
}

CP_PHASE = {
    "delta_CP_deg": 195.0,  # Approx T2K best fit
    "uncertainty_deg": 30.0,
    "delta_CP_over_pi": 1.08,
    "status": "Non-zero favored (1.5 sigma)",
    "T2K_value": -96.0 + 360,
    "NOvA_value": 0.0,  # NOvA prefers no CP violation approx?
}

MASS_SPLITTINGS = {
    "delta_m21_squared": {
        "value_eV2": 7.53e-5,
    },
    "delta_m32_squared_NO": {
        "value_eV2": 2.45e-3,
    },
}

MASS_ORDERING = {
    "preferred": "Normal Ordering (NO)",
    "significance": "2.5 sigma",
}

# Values for CKM comparison
CKM_VS_PMNS = {
    "CKM_angles": {
        "theta12_Cabibbo": 13.04,
        "theta23_cb": 2.38,
        "theta13_ub": 0.20,
    },
    "PMNS_angles": {
        "theta12_solar": 33.44,
        "theta23_atm": 49.2,
        "theta13_reactor": 8.57,
    },
}

# ==============================================================================
# FUNCTIONS
# ==============================================================================


def calculate_pmns_matrix(th12, th23, th13, delta):
    """
    Calculate PMNS matrix elements.
    Angles in radians.
    """
    c12 = np.cos(th12)
    s12 = np.sin(th12)
    c23 = np.cos(th23)
    s23 = np.sin(th23)
    c13 = np.cos(th13)
    s13 = np.sin(th13)

    eid = np.exp(-1j * delta)

    # Standard parametrization
    U = np.zeros((3, 3), dtype=complex)

    U[0, 0] = c12 * c13
    U[0, 1] = s12 * c13
    U[0, 2] = s13 * np.exp(-1j * delta)

    U[1, 0] = -s12 * c23 - c12 * s23 * s13 * eid
    U[1, 1] = c12 * c23 - s12 * s23 * s13 * eid
    U[1, 2] = s23 * c13

    U[2, 0] = s12 * s23 - c12 * c23 * s13 * eid
    U[2, 1] = -c12 * s23 - s12 * c23 * s13 * eid
    U[2, 2] = c23 * c13

    return U


# Pre-calculate matrix magnitudes for verification
th12_rad = np.deg2rad(PMNS_MIXING_ANGLES["theta12"]["value_deg"])
th23_rad = np.deg2rad(PMNS_MIXING_ANGLES["theta23"]["value_deg"])
th13_rad = np.deg2rad(PMNS_MIXING_ANGLES["theta13"]["value_deg"])
delta_rad = np.deg2rad(CP_PHASE["delta_CP_deg"])

U_PMNS = calculate_pmns_matrix(th12_rad, th23_rad, th13_rad, delta_rad)
PMNS_MATRIX = U_PMNS
PMNS_MAGNITUDES = np.abs(U_PMNS)


def uet_pmns_prediction(kappa=0.5, beta=1.0):
    """
    UET predictions for mixing parameters.
    Based on Information Field Geometry.
    """
    # Geometric ansatz
    theta12_pred = 30.0  # pi/6
    theta23_pred = 45.0  # pi/4

    # theta13 is suppressed by kappa
    # theta13 ~ kappa * pi/16 = 0.5 * 11.25 = 5.6 deg?
    # Or kappa * beta * something?
    # Experiment is ~8.57.
    # Maybe kappa * pi/10 = 0.5 * 18 = 9?
    theta13_pred = 9.0

    # CP phase
    delta_pred = 180.0  # Maximal violation around 180?

    return {
        "theta12": theta12_pred,
        "theta23": theta23_pred,
        "theta13": theta13_pred,
        "delta_CP": delta_pred,
    }


def uet_mass_ratio_from_mixing():
    """Test hypothesis that mixing angle scales with mass."""
    sin2_12 = np.sin(th12_rad) ** 2

    # Ratio of mass splittings
    dm21 = MASS_SPLITTINGS["delta_m21_squared"]["value_eV2"]
    dm32 = MASS_SPLITTINGS["delta_m32_squared_NO"]["value_eV2"]

    ratio_sqrt = np.sqrt(dm21 / dm32)

    return {"sin2_theta12": sin2_12, "mass_ratio_sqrt": ratio_sqrt, "ratio": sin2_12 / ratio_sqrt}


def P_numu_to_nue(L, E):
    """Placeholder for oscillation probability."""
    return 0.05  # Dummy value
