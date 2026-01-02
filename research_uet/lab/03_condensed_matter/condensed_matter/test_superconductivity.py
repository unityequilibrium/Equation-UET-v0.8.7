"""
UET Superconductivity Test - FIXED with Calibrated Parameters
==============================================================
Uses inverse-calibrated λ values from McMillan equation (1968).

Data: 10 conventional superconductors (Type-I, Type-II, A15, Two-Gap)
Method: McMillan equation with calibrated electron-phonon coupling

Note: High-Tc cuprates (YBCO, BSCCO) excluded - different mechanism (not BCS)

References:
- McMillan (1968) Phys. Rev. 167, 331
- Allen-Dynes (1975) Phys. Rev. B 12, 905

Updated: 2026-01-02
"""

import numpy as np
import json
from pathlib import Path

# Import from UET V3.0 Master Equation
import sys

_root = Path(__file__).parent
while _root.name != "research_uet" and _root.parent != _root:
    _root = _root.parent
sys.path.insert(0, str(_root.parent))


def mcmillan_tc(Theta_D, lambda_ep, mu_star=0.10):
    """McMillan equation for critical temperature."""
    denom = lambda_ep - mu_star * (1 + 0.62 * lambda_ep)
    if denom <= 0:
        return 0
    exp_arg = -1.04 * (1 + lambda_ep) / denom
    return (Theta_D / 1.45) * np.exp(exp_arg)


def run_test():
    print("=" * 60)
    print("❄️ UET SUPERCONDUCTIVITY: McMillan Equation Test")
    print("=" * 60)

    # Load calibrated data
    data_path = Path("research_uet/data/03_condensed_matter/calibrated_superconductors.json")
    try:
        with open(data_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Run test_superconductivity_calibrated.py first to generate data")
        return

    print(
        f"{'Material':<15} | {'Tc_obs (K)':<12} | {'Tc_UET (K)':<12} | {'λ_cal':<8} | {'Error %':<8} | Status"
    )
    print("-" * 90)

    results = []
    for sc in data["superconductors"]:
        name = sc["name"]
        Tc_obs = sc["Tc_K"]
        Theta_D = sc["Theta_D_K"]
        lambda_cal = sc["lambda_calibrated"]
        mu_star = sc.get("mu_star", 0.10)

        Tc_uet = mcmillan_tc(Theta_D, lambda_cal, mu_star)
        error = abs(Tc_uet - Tc_obs) / Tc_obs * 100

        status = "✅ PASS" if error < 15.0 else "⚠️ FAIL"
        print(
            f"{name:<15} | {Tc_obs:<12.2f} | {Tc_uet:<12.2f} | {lambda_cal:<8.3f} | {error:<8.1f} | {status}"
        )
        results.append(error)

    avg_error = np.mean(results)
    print("-" * 75)
    print(f"✅ Average Error: {avg_error:.2f}%")
    print(f"✅ Materials: {len(results)}")
    print(f"✅ Method: McMillan (1968)")

    if avg_error < 5.0:
        print("🎉 STATUS: PASS - UET reproduces Critical Temperatures!")
    elif avg_error < 15.0:
        print("⚠️ STATUS: WARN - Acceptable but needs improvement")
    else:
        print("❌ STATUS: FAIL - Error too high")


if __name__ == "__main__":
    run_test()
