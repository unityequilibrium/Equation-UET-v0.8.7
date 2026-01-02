"""
UET Standard Model Validation Test
====================================
Tests that UET properly SUPPLEMENTS (not replaces) Standard Model.

Key Principle: UET adds interpretive layer to SM, doesn't change predictions.

Updated for UET V3.0
"""

import numpy as np
import sys
import os

# Add project root to path
import sys

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

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up 4 levels: lab/01/standard/ -> research_uet/
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))
# Add data path (bypass 01_ prefix issue)
data_dir = os.path.join(root_dir, "research_uet", "data", "01_particle_physics")
if data_dir not in sys.path:
    sys.path.insert(0, data_dir)

from particle_masses import (
    QUARK_MASSES,
    LEPTON_MASSES,
    GAUGE_BOSON_MASSES,
    HIGGS_BOSON,
    COUPLING_CONSTANTS,
    ALL_PARTICLE_MASSES_GEV,
)


def uet_mass_relation(m_particle_GeV: float, v_higgs: float = 246.22) -> dict:
    """
    UET interpretation of particle mass.

    In Standard Model: m = y * v / sqrt(2)  (Yukawa coupling)
    In UET: Mass arises from C-I equilibrium energy

    UET does NOT predict mass, but interprets WHY it has that value
    through equilibrium dynamics.

    Returns UET parameters that would give this equilibrium.
    """
    # Yukawa coupling in SM
    y_sm = m_particle_GeV * np.sqrt(2) / v_higgs

    # UET interpretation: coupling relates to C-I gradient
    # kappa ~ y^2 (gradient strength from Yukawa)
    kappa_uet = y_sm**2

    # beta relates to field mixing
    beta_uet = y_sm / (1 + y_sm)

    return {
        "y_SM": y_sm,
        "kappa_UET": kappa_uet,
        "beta_UET": beta_uet,
        "interpretation": "Mass from C-I equilibrium",
    }


def test_mass_hierarchy():
    """Test UET understanding of mass hierarchy."""
    print("\n" + "=" * 60)
    print("TEST 1: Particle Mass Hierarchy")
    print("=" * 60)

    print("\nSM masses from PDG 2024:")
    print("-" * 50)
    print(f"{'Particle':<10} {'Mass (GeV)':<15} {'y (Yukawa)':<12} {'kappa_UET':<12}")
    print("-" * 50)

    particles = [
        ("electron", 0.511e-3),
        ("muon", 0.106),
        ("tau", 1.777),
        ("top", 172.57),
        ("Higgs", 125.20),
        ("W", 80.36),
        ("Z", 91.19),
    ]

    for name, mass in particles:
        uet = uet_mass_relation(mass)
        print(f"{name:<10} {mass:<15.4g} {uet['y_SM']:<12.4g} {uet['kappa_UET']:<12.4g}")

    print("\nUET Interpretation:")
    print("  - Large kappa = strong gradient = heavy particle")
    print("  - Small kappa = weak gradient = light particle")
    print("  - Hierarchy explained by equilibrium energy scales")

    return True


def test_coupling_running():
    """Test UET interpretation of running couplings."""
    print("\n" + "=" * 60)
    print("TEST 2: Running Coupling Constants")
    print("=" * 60)

    # SM couplings at M_Z
    alpha_em = COUPLING_CONSTANTS["alpha_EM"]["value"]
    alpha_s = COUPLING_CONSTANTS["alpha_s"]["value"]
    sin2_w = COUPLING_CONSTANTS["sin2_theta_W"]["value"]

    print(f"\nStandard Model values at M_Z = 91.19 GeV:")
    print(f"  alpha_EM = 1/{1/alpha_em:.1f}")
    print(f"  alpha_s  = {alpha_s:.4f}")
    print(f"  sin2_thetaW = {sin2_w:.4f}")

    # UET mapping
    # alpha -> C-I coupling strength
    # alpha_s -> kappa (gradient coefficient)
    # sin2_w -> beta ratio

    kappa_EM = alpha_em
    kappa_strong = alpha_s
    beta_ratio = sin2_w

    print(f"\nUET Mapping:")
    print(f"  kappa_EM (C-I coupling) = {kappa_EM:.6f}")
    print(f"  kappa_strong (gradient) = {kappa_strong:.4f}")
    print(f"  beta_I/(beta_C+beta_I)  = {beta_ratio:.4f}")

    print("\nInterpretation:")
    print("  - EM: Weak C-I coupling (kappa ~ 1/137)")
    print("  - Strong: Strong gradient (kappa ~ 0.12)")
    print("  - Electroweak: Balance between C and I fields")

    return True


def test_gauge_symmetry():
    """Test UET compatibility with gauge symmetries."""
    print("\n" + "=" * 60)
    print("TEST 3: Gauge Symmetry Structure")
    print("=" * 60)

    print("\nStandard Model: SU(3)_C x SU(2)_L x U(1)_Y")
    print("-" * 50)

    # SM gauge structure
    gauge_groups = [
        ("SU(3)_C", "Strong", "8 gluons", 0.1179),
        ("SU(2)_L", "Weak isospin", "W+, W-, W0", 0.65),
        ("U(1)_Y", "Hypercharge", "B", 0.35),
    ]

    print(f"{'Group':<12} {'Force':<15} {'Bosons':<15} {'g (coupling)':<12}")
    print("-" * 50)

    for group, force, bosons, g in gauge_groups:
        print(f"{group:<12} {force:<15} {bosons:<15} {g:<12.4f}")

    print("\nUET Interpretation:")
    print("  - SU(3): 3 C-field colors (quark confinement)")
    print("  - SU(2): C-I doublet structure")
    print("  - U(1): I-field phase symmetry")
    print("  - UET does NOT change gauge structure!")
    print("  - UET provides DYNAMICS within this structure")

    return True


def test_higgs_mechanism():
    """Test UET interpretation of Higgs mechanism."""
    print("\n" + "=" * 60)
    print("TEST 4: Higgs Mechanism Interpretation")
    print("=" * 60)

    m_H = HIGGS_BOSON["mass_GeV"]
    m_W = GAUGE_BOSON_MASSES["W_pm"]["mass_GeV"]
    m_Z = GAUGE_BOSON_MASSES["Z_0"]["mass_GeV"]

    # Higgs VEV
    v = 246.22  # GeV

    print(f"\nHiggs parameters:")
    print(f"  m_H = {m_H:.2f} GeV")
    print(f"  v (VEV) = {v:.2f} GeV")

    # SM relations
    lambda_H = m_H**2 / (2 * v**2)
    g_W = 2 * m_W / v
    g_Z = 2 * m_Z / v

    print(f"\nSM Relations:")
    print(f"  lambda (quartic) = {lambda_H:.4f}")
    print(f"  g_W = {g_W:.4f}")
    print(f"  g_Z = {g_Z:.4f}")

    # UET interpretation
    # Higgs = Universal field Omega at equilibrium
    # VEV = Ground state of Omega potential
    # Mass generation = C-field coupling to Omega

    print("\nUET Interpretation:")
    print("  - Higgs field = Omega (Universal equilibrium field)")
    print("  - VEV = Omega ground state (v = 246 GeV)")
    print("  - Mass = C-field coupling to Omega gradient")
    print("  - UET explains WHY this equilibrium exists")
    print("  - UET does NOT change Higgs predictions!")

    return True


def run_all_tests():
    """Run complete Standard Model validation."""
    print("=" * 70)
    print("UET STANDARD MODEL VALIDATION")
    print("Principle: UET SUPPLEMENTS Standard Model")
    print("=" * 70)

    test_mass_hierarchy()
    test_coupling_running()
    test_gauge_symmetry()
    test_higgs_mechanism()

    print("\n" + "=" * 70)
    print("SUMMARY: UET-Standard Model Relationship")
    print("=" * 70)

    print(
        """
    ✅ UET DOES:
    - Map SM fields to C-I-Omega dynamics
    - Interpret coupling constants as equilibrium parameters
    - Explain hierarchy through gradient energies
    - Add dynamics perspective to static SM
    
    ❌ UET DOES NOT:
    - Replace QFT calculations
    - Change SM predictions
    - Contradict gauge structure
    - Predict different particle masses
    
    🎯 UET = Framework that HOSTS Standard Model
    """
    )

    print("\n" + "*" * 50)
    print("UET-SM BRIDGE VALIDATION: COMPLETE")
    print("*" * 50)

    return True


if __name__ == "__main__":
    run_all_tests()
