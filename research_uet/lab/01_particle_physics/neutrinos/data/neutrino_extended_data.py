"""
Neutrino Extended Data - REAL Experimental Data
================================================
Sources:
- KATRIN 2025: https://www.katrin.kit.edu
- Borexino Collaboration
- PDG 2024

Updated: 2026-01-02
"""

# KATRIN 2025 Results (Direct Neutrino Mass Measurement)
# Source: KATRIN Collaboration, "Direct neutrino mass measurement"
KATRIN_RESULTS = {
    "mass_limit_eV": 0.45,  # 90% C.L. upper limit
    "sensitivity_eV": 0.4,
    "source": "KATRIN Collaboration 2025",
    "technique": "Tritium beta decay endpoint",
    "note": "Best direct measurement as of 2025",
}

# Solar Neutrino Data from Borexino
# Source: Borexino Collaboration, Nature 2020
SOLAR_NEUTRINOS_BOREXINO = {
    "CNO_cycle": {
        "flux_cm2_s": 7.0e9,  # CNO neutrino flux
        "uncertainty": 3.0e9,
        "significance": "5σ detection",
        "source": "Borexino 2020 Nature",
    },
    "pp_chain": {
        "pp_flux": 6.1e10,  # pp neutrino flux cm^-2 s^-1
        "Be7_flux": 4.84e9,
        "pep_flux": 1.44e8,
        "source": "Borexino Phase-II",
    },
}

# Cosmic Neutrino Background (Theoretical)
CNB_DATA = {
    "temperature_K": 1.95,  # ~1.95 K (From Big Bang)
    "density_per_cm3": 336,  # Total neutrino + antineutrino
    "status": "Not yet detected directly",
    "source": "Standard Cosmology",
}

# Neutrino Oscillation Parameters (PDG 2024)
OSCILLATION_PARAMS = {
    "sin2_theta12": 0.304,
    "sin2_theta23": 0.573,
    "sin2_theta13": 0.02220,
    "delta_m21_sq_eV2": 7.53e-5,
    "delta_m32_sq_eV2": 2.453e-3,
    "source": "PDG 2024",
}
