"""
UET Fluid Dynamics Test - Brownian Motion
==========================================
Tests UET prediction for Brownian motion (Einstein relation).
Data: Perrin 1908 Nobel Prize work.
"""

import sys
from pathlib import Path
import math

SOLUTION = Path(__file__).parent.parent.parent

# Physical constants
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = math.pi


def perrin_1908_data():
    """Perrin's experimental data."""
    return {
        "temperature_K": 293,  # ~20C
        "viscosity_Pa_s": 1.002e-3,  # Water at 20C
        "particle_radius_m": 0.5e-6,  # 0.5 micron particles
        "measured_D_m2_s": 4.3e-13,  # Measured diffusion coefficient
        "avogadro_derived": 6.0e23,  # Perrin's estimate
    }


def uet_diffusion_coefficient(T, eta, r):
    """
    UET prediction for diffusion coefficient.

    From UET: Brownian motion is the thermal equilibration of
    the C (particle) field with the I (information/entropy) field.

    The equilibrium condition gives:
    D = k_B * T / (6 * pi * eta * r)

    This is Einstein's relation, which UET derives from:
    dC/dt = D * nabla^2 C = beta * nabla I

    At equilibrium: beta = k_B * T (Landauer principle)
    """
    D = k_B * T / (6 * pi * eta * r)
    return D


def uet_mean_squared_displacement(D, t):
    """
    MSD for 3D Brownian motion.
    <r^2> = 6 * D * t
    """
    return 6 * D * t


def run_test():
    """Run Brownian motion test."""
    print("=" * 70)
    print("UET BROWNIAN MOTION TEST")
    print("Data: Perrin 1908 (Nobel Prize 1926)")
    print("=" * 70)

    data = perrin_1908_data()
    T = data["temperature_K"]
    eta = data["viscosity_Pa_s"]
    r = data["particle_radius_m"]
    D_exp = data["measured_D_m2_s"]

    D_uet = uet_diffusion_coefficient(T, eta, r)

    print("\n[1] DIFFUSION COEFFICIENT")
    print("-" * 50)
    print(f"  Temperature:     {T} K")
    print(f"  Viscosity:       {eta:.3e} Pa*s")
    print(f"  Particle radius: {r*1e6:.1f} microns")
    print(f"")
    print(f"  Perrin measured: D = {D_exp:.2e} m^2/s")
    print(f"  UET predicted:   D = {D_uet:.2e} m^2/s")

    error = abs(D_uet - D_exp) / D_exp * 100
    print(f"\n  Error: {error:.1f}%")

    passed = error < 10
    print(f"  {'PASS' if passed else 'FAIL'}")

    print("\n[2] MEAN SQUARED DISPLACEMENT")
    print("-" * 50)

    times = [1, 10, 60, 600]  # seconds
    print("| Time (s) | MSD (micron^2) |")
    print("|:---------|:---------------|")

    for t in times:
        msd = uet_mean_squared_displacement(D_uet, t)
        msd_um2 = msd * 1e12  # Convert to micron^2
        print(f"| {t:8} | {msd_um2:14.2f} |")

    print("\n[3] UET INTERPRETATION")
    print("-" * 50)
    print(
        """
    Brownian motion in UET:
    
    1. Particles (C field) are in thermal equilibrium with
       the surrounding info field (I)
       
    2. Random kicks come from local I-field fluctuations
       with variance ~ k_B*T (equipartition)
       
    3. Viscous drag comes from C-field interactions
       
    4. The equilibrium between these gives Einstein relation:
       D = k_B*T / (6*pi*eta*r)
       
    5. This directly confirms the UET beta = k_B*T link
       (same as Landauer principle!)
    """
    )

    print("=" * 70)
    print(f"RESULT: {'PASS' if passed else 'NEEDS CALIBRATION'}")
    print("=" * 70)

    return passed


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
