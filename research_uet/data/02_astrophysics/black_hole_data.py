"""
Black Hole Experimental Data
============================
From Event Horizon Telescope (EHT), LIGO, and X-ray observations.

Sources:
- EHT Collaboration 2019, 2022, 2024
- LIGO-Virgo GW catalogs
"""

import json
import os


# Load data from external JSON
def _load_data():
    # Path relative to: research_uet/data_vault/astrophysics/black_hole_data.py
    # Json is in: research_uet/data_vault/sources/black_hole_data.json
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "references", "black_hole_data.json")

    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


_data = _load_data()

# ============================================
# SUPERMASSIVE BLACK HOLES (EHT)
# ============================================

M87_BLACK_HOLE = _data["supermassive"][0]
SGR_A_BLACK_HOLE = _data["supermassive"][1]

# ============================================
# STELLAR BLACK HOLES (X-ray)
# ============================================

STELLAR_BLACK_HOLES = [
    (x["name"], x["mass_solar"], x["error"], x["distance_kpc"], x["source"])
    for x in _data["stellar"]
]

# ============================================
# GRAVITATIONAL WAVE BLACK HOLES (LIGO)
# ============================================

LIGO_BLACK_HOLES = [
    (x["event"], x["m1"], x["m2"], x["final_mass"], x["distance_Mpc"])
    for x in _data["gravitational_wave"]
]

# ============================================
# SCHWARZSCHILD RADIUS FORMULA
# ============================================


def schwarzschild_radius_km(mass_solar: float) -> float:
    """
    Schwarzschild radius: r_s = 2GM/c^2

    For solar mass: r_s ~ 3 km
    """
    return 2.95 * mass_solar  # km


def event_horizon_angular_size_uas(mass_solar: float, distance_Mpc: float) -> float:
    """
    Angular size of event horizon in microarcseconds.

    θ = r_s / d
    """
    r_s_km = schwarzschild_radius_km(mass_solar)
    d_km = distance_Mpc * 3.086e19  # Mpc to km
    theta_rad = r_s_km / d_km
    theta_uas = theta_rad * 2.063e11  # rad to microarcseconds
    return theta_uas


# ============================================
# HAWKING TEMPERATURE (for quantum effects)
# ============================================


def hawking_temperature_K(mass_solar: float) -> float:
    """
    Hawking temperature: T_H = hbar c^3 / (8pi G M k_B)

    For solar mass: T ~ 6e-8 K (unmeasurable)
    For primordial BH (1e12 kg): T ~ 1e11 K (hot!)
    """
    # T_H ~ 6.17e-8 * (M_sun / M)
    return 6.17e-8 / mass_solar  # Kelvin


if __name__ == "__main__":
    print("=" * 60)
    print("BLACK HOLE DATA SUMMARY")
    print("=" * 60)

    print("\nSupermassive Black Holes (EHT):")
    print(f"  M87*: {M87_BLACK_HOLE['mass_solar']:.1e} Msun")
    print(f"  Sgr A*: {SGR_A_BLACK_HOLE['mass_solar']:.1e} Msun")

    print("\nStellar Black Holes:")
    for name, mass, _, _, _ in STELLAR_BLACK_HOLES[:3]:
        print(f"  {name}: {mass} Msun")

    print("\nLIGO Mergers:")
    for event, m1, m2, mf, _ in LIGO_BLACK_HOLES[:3]:
        print(f"  {event}: {m1}+{m2} -> {mf} Msun")

    print(f"\nSchwarzschild radius (1 Msun): {schwarzschild_radius_km(1):.2f} km")
    print(f"Hawking temp (1 Msun): {hawking_temperature_K(1):.2e} K")
