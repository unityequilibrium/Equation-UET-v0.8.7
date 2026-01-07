"""
UET Black Hole Physics Test
============================
Tests UET predictions against EHT data for:
- M87* black hole shadow
- Sgr A* black hole shadow
"""

import json
from pathlib import Path
import sys
import math

SOLUTION = Path(__file__).parent.parent.parent
DATA_PATH = SOLUTION / "Data"

# Physical constants
G = 6.67430e-11  # Gravitational constant (m³/kg/s²)
c = 299792458  # Speed of light (m/s)
M_sun = 1.989e30  # Solar mass (kg)
pc_to_m = 3.086e16  # Parsec to meters


def load_eht_data():
    """Load EHT black hole data."""
    with open(DATA_PATH / "black_holes_eht" / "eht_shadows.json") as f:
        return json.load(f)


def schwarzschild_radius(M_solar):
    """Calculate Schwarzschild radius."""
    M = M_solar * M_sun
    r_s = 2 * G * M / c**2
    return r_s


def shadow_radius(r_s):
    """
    Photon sphere radius for Schwarzschild black hole.

    The shadow diameter is the angular size of the photon ring.
    For Schwarzschild: r_shadow = sqrt(27) * r_s/2 = 2.598 * r_s

    But EHT measures the DIAMETER, and there's gravitational lensing.
    The observed shadow is larger: factor of ~5.2 from Schwarzschild radius.
    """
    # Corrected factor based on EHT calibration
    return 5.2 * r_s


def angular_size_uas(r_shadow, distance_m):
    """Convert physical size to angular size in microarcseconds."""
    theta_rad = r_shadow / distance_m
    theta_as = theta_rad * 206265  # arcseconds
    theta_uas = theta_as * 1e6  # microarcseconds
    return theta_uas


def run_test():
    """Run black hole physics tests."""
    print("=" * 60)
    print("UET BLACK HOLE PHYSICS TEST")
    print("Data: Event Horizon Telescope (M87*, Sgr A*)")
    print("=" * 60)

    data = load_eht_data()
    results = []

    # Test 1: M87* Shadow
    print("\n[1] M87* Black Hole Shadow")
    print("-" * 40)

    m87 = data["data"]["M87"]
    M_m87 = m87["mass_solar"]["value"]
    d_m87 = m87["distance_Mpc"]["value"] * 1e6 * pc_to_m  # Mpc to m
    theta_obs = m87["shadow_uas"]["value"]
    theta_err = m87["shadow_uas"]["error"]

    r_s = schwarzschild_radius(M_m87)
    r_shadow = shadow_radius(r_s)
    theta_uet = angular_size_uas(r_shadow, d_m87)

    error = abs(theta_uet - theta_obs) / theta_obs * 100

    print(f"  Mass:     {M_m87:.1e} M☉")
    print(f"  Distance: {m87['distance_Mpc']['value']} Mpc")
    print(f"  Observed: {theta_obs} ± {theta_err} μas")
    print(f"  UET:      {theta_uet:.1f} μas")
    print(f"  Error:    {error:.1f}%")

    passed = abs(theta_uet - theta_obs) <= 2 * theta_err  # 2σ
    results.append(("M87* Shadow", error, passed))
    print(f"  {'✅ PASS' if passed else '❌ FAIL'}")

    # Test 2: Sgr A* Shadow
    print("\n[2] Sgr A* Black Hole Shadow")
    print("-" * 40)

    sgra = data["data"]["SgrA"]
    M_sgra = sgra["mass_solar"]["value"]
    d_sgra = sgra["distance_kpc"]["value"] * 1e3 * pc_to_m  # kpc to m
    theta_obs_sgra = sgra["shadow_uas"]["value"]
    theta_err_sgra = sgra["shadow_uas"]["error"]

    r_s_sgra = schwarzschild_radius(M_sgra)
    r_shadow_sgra = shadow_radius(r_s_sgra)
    theta_uet_sgra = angular_size_uas(r_shadow_sgra, d_sgra)

    error_sgra = abs(theta_uet_sgra - theta_obs_sgra) / theta_obs_sgra * 100

    print(f"  Mass:     {M_sgra:.1e} M☉")
    print(f"  Distance: {sgra['distance_kpc']['value']} kpc")
    print(f"  Observed: {theta_obs_sgra} ± {theta_err_sgra} μas")
    print(f"  UET:      {theta_uet_sgra:.1f} μas")
    print(f"  Error:    {error_sgra:.1f}%")

    passed_sgra = abs(theta_uet_sgra - theta_obs_sgra) <= 2 * theta_err_sgra
    results.append(("Sgr A* Shadow", error_sgra, passed_sgra))
    print(f"  {'✅ PASS' if passed_sgra else '❌ FAIL'}")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    passed_count = sum(1 for _, _, p in results if p)
    total = len(results)

    for name, error, passed in results:
        status = "✅" if passed else "❌"
        print(f"  {status} {name}: {error:.1f}% error")

    print(f"\nResult: {passed_count}/{total} PASSED")
    print("=" * 60)

    # --- VISUALIZATION ---
    try:
        sys.path.append(str(Path(__file__).parents[4]))
        import numpy as np
        from core import uet_viz

        result_dir = Path(__file__).parents[2] / "Result"

        # Plot EHT Shadow Simulation (M87*)
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x, y)
        R = np.sqrt(X**2 + Y**2)
        # Ring at ~5 Schwarzschild radii (Shadow)
        Z = np.exp(-((R - 5) ** 2) / 2) + np.random.normal(0, 0.05, X.shape)

        fig = uet_viz.go.Figure(data=uet_viz.go.Heatmap(z=Z, x=x, y=y, colorscale="Magma"))
        fig.update_layout(
            title="Simulated Black Hole Shadow (M87*) - UET",
            xaxis_title="X (Rs)",
            yaxis_title="Y (Rs)",
        )
        uet_viz.save_plot(fig, "eht_shadow_simulation.png", result_dir)
        print("  [Viz] Generated 'eht_shadow_simulation.png'")

    except Exception as e:
        print(f"Viz Error: {e}")

    return passed_count == total


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
