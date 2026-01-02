"""
Neutrino Oscillation Parameters
===============================
PDG 2024 Neutrino Mixing Parameters

Reference: Phys. Rev. D 110, 030001 (2024)
           "Neutrino Mixing" section

Updated for UET V3.0
"""


# Import from UET V3.0 Master Equation
import sys
from pathlib import Path
_root = Path(__file__).parent
while _root.name != "research_uet" and _root.parent != _root:
    _root = _root.parent
sys.path.insert(0, str(_root.parent))
try:
    from research_uet.core.uet_master_equation import (
        UETParameters, SIGMA_CRIT, strategic_boost, potential_V, KAPPA_BEKENSTEIN
    )
except ImportError:
    pass  # Use local definitions if not available

import numpy as np

# ================================================================
# NEUTRINO MASSES AND MASS DIFFERENCES
# ================================================================

MASS_SQUARED_DIFFERENCES = {
    # Solar mass difference (Δm²₂₁)
    "delta_m21_squared": {
        "value": 7.53e-5,  # eV²
        "uncertainty_plus": 0.18e-5,
        "uncertainty_minus": 0.18e-5,
        "unit": "eV²",
        "source": "Solar + KamLAND",
        "reference": "PDG 2024",
    },
    # Atmospheric mass difference (|Δm²₃₂|)
    "delta_m32_squared_normal": {
        "value": 2.453e-3,  # eV²
        "uncertainty": 0.033e-3,
        "unit": "eV²",
        "ordering": "Normal (m₃ > m₂ > m₁)",
        "source": "Atmospheric + Accelerator",
        "reference": "PDG 2024",
    },
    "delta_m32_squared_inverted": {
        "value": -2.536e-3,  # eV² (negative for inverted)
        "uncertainty": 0.034e-3,
        "unit": "eV²",
        "ordering": "Inverted (m₂ > m₁ > m₃)",
        "reference": "PDG 2024",
    },
}

# ================================================================
# MIXING ANGLES (PMNS MATRIX)
# ================================================================

MIXING_ANGLES = {
    # Solar angle θ₁₂
    "theta_12": {
        "sin2_theta": 0.307,
        "uncertainty": 0.013,
        "theta_degrees": np.degrees(np.arcsin(np.sqrt(0.307))),
        "source": "Solar + KamLAND",
        "reference": "PDG 2024",
    },
    # Atmospheric angle θ₂₃
    "theta_23_normal": {
        "sin2_theta": 0.546,
        "uncertainty_plus": 0.021,
        "uncertainty_minus": 0.023,
        "theta_degrees": np.degrees(np.arcsin(np.sqrt(0.546))),
        "octant": "Upper (θ₂₃ > 45°)",
        "reference": "PDG 2024 (Normal Ordering)",
    },
    "theta_23_inverted": {
        "sin2_theta": 0.539,
        "uncertainty_plus": 0.022,
        "uncertainty_minus": 0.022,
        "reference": "PDG 2024 (Inverted Ordering)",
    },
    # Reactor angle θ₁₃
    "theta_13": {
        "sin2_theta": 0.0220,
        "uncertainty": 0.0007,
        "theta_degrees": np.degrees(np.arcsin(np.sqrt(0.0220))),
        "source": "Daya Bay, RENO, Double Chooz",
        "reference": "PDG 2024",
    },
}

# ================================================================
# CP VIOLATION PHASE
# ================================================================

CP_PHASE = {
    "delta_CP": {
        "value_degrees": 195,  # Central value
        "range_degrees": (120, 369),  # 3σ range
        "value_radians": np.radians(195),
        "status": "Non-zero CP violation indicated",
        "source": "T2K + NOvA",
        "reference": "PDG 2024",
    },
}

# ================================================================
# NEUTRINO PROPERTIES
# ================================================================

NEUTRINO_PROPERTIES = {
    "mass_hierarchy": {
        "current_preference": "Normal ordering slightly preferred",
        "confidence": "~2-3σ",
        "experiments": ["NOvA", "T2K", "Super-Kamiokande"],
    },
    "sum_of_masses": {
        "cosmological_upper_limit": 0.12,  # eV (Planck 2018)
        "unit": "eV",
        "source": "CMB + BAO",
    },
    "dirac_vs_majorana": {
        "status": "Unknown",
        "test": "Neutrinoless double beta decay",
    },
}

# ================================================================
# PMNS MATRIX (Approximate values)
# ================================================================


def get_pmns_matrix():
    """Calculate PMNS matrix from mixing angles."""
    s12 = np.sqrt(0.307)
    c12 = np.sqrt(1 - 0.307)
    s23 = np.sqrt(0.546)
    c23 = np.sqrt(1 - 0.546)
    s13 = np.sqrt(0.0220)
    c13 = np.sqrt(1 - 0.0220)
    delta = np.radians(195)

    # Simplified PMNS (ignoring CP phase for magnitude)
    U = np.array(
        [
            [c12 * c13, s12 * c13, s13],
            [
                -s12 * c23 - c12 * s23 * s13,
                c12 * c23 - s12 * s23 * s13,
                s23 * c13,
            ],
            [
                s12 * s23 - c12 * c23 * s13,
                -c12 * s23 - s12 * c23 * s13,
                c23 * c13,
            ],
        ]
    )
    return U


# ================================================================
# UET INTERPRETATION
# ================================================================

UET_INTERPRETATION = {
    "concept": "Neutrino as pure Information carrier",
    "mechanism": """
        In UET framework:
        - Neutrinos are massless in βCI = 0 limit
        - Mass arises from I-field coupling
        - Oscillation = Information wave interference
        
        Flavor mixing = I-field phase evolution
        
        The tiny neutrino mass reflects weak I-field coupling:
        m_ν / m_e ~ β_ν / β_e ~ 10⁻⁶
    """,
    "prediction": """
        Neutrino oscillation preserves total Information.
        Mass differences = I-field energy level spacing.
        CP violation = I-field phase asymmetry.
    """,
}


# ================================================================
# HELPER FUNCTIONS
# ================================================================


def get_mass_difference(name="atmospheric"):
    """Return mass squared difference in eV²."""
    if name == "solar":
        return MASS_SQUARED_DIFFERENCES["delta_m21_squared"]["value"]
    elif name == "atmospheric":
        return MASS_SQUARED_DIFFERENCES["delta_m32_squared_normal"]["value"]
    else:
        raise ValueError(f"Unknown mass difference: {name}")


def oscillation_probability(L_km, E_GeV, dm2_eV2=2.45e-3, sin2_2theta=1.0):
    """
    Calculate neutrino oscillation probability.

    P(ν_μ → ν_τ) ≈ sin²(2θ) × sin²(1.27 × Δm² × L / E)
    """
    arg = 1.27 * dm2_eV2 * L_km / E_GeV
    return sin2_2theta * np.sin(arg) ** 2


if __name__ == "__main__":
    print("=" * 60)
    print("Neutrino Oscillation Parameters (PDG 2024)")
    print("=" * 60)

    print("\nMass Squared Differences:")
    print(f"  Δm²₂₁ = {get_mass_difference('solar'):.2e} eV²")
    print(f"  Δm²₃₂ = {get_mass_difference('atmospheric'):.2e} eV²")

    print("\nMixing Angles (sin²θ):")
    print(f"  θ₁₂: {MIXING_ANGLES['theta_12']['sin2_theta']:.3f}")
    print(f"  θ₂₃: {MIXING_ANGLES['theta_23_normal']['sin2_theta']:.3f}")
    print(f"  θ₁₃: {MIXING_ANGLES['theta_13']['sin2_theta']:.4f}")

    print("\nCP Phase:")
    print(f"  δ_CP ≈ {CP_PHASE['delta_CP']['value_degrees']}°")

    print("\nPMNS Matrix |U|:")
    U = get_pmns_matrix()
    for row in np.abs(U):
        print(f"  {row[0]:.3f}  {row[1]:.3f}  {row[2]:.3f}")
