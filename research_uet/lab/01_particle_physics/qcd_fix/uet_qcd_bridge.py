"""
UET-QCD Bridge Model
====================
Corrected α_s model that combines standard QCD running
with UET Information correction.

Key Insight:
α_UET(Q) = α_QCD(Q) × (1 + β_UET × I(Q))

Where I(Q) represents the Information density at scale Q.
At high Q, quarks are nearly free → I(Q) vanishes.
At low Q, confinement → I(Q) contributes.

Updated for UET V3.0
"""

import numpy as np
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

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.qcd_alpha_s_data import (
    ALPHA_S_DATA,
    ALPHA_S_MZ,
    QCD_PARAMS,
    alpha_s_qcd,
    get_n_f,
    get_alpha_s_table,
)


# ================================================================
# UET-QCD BRIDGE MODEL
# ================================================================


def alpha_s_uet_v1(Q, beta_uet=0.05, I_scale=1.0):
    """
    UET-enhanced QCD running coupling v1.

    α_UET(Q) = α_QCD(Q) × (1 + β_UET × I(Q))

    I(Q) = I_scale / (1 + Q/Λ)  -- Info density decreases at high Q

    Parameters:
    - Q: Energy scale (GeV)
    - beta_uet: UET coupling strength
    - I_scale: Information density scale
    """
    n_f = get_n_f(Q)
    Lambda = QCD_PARAMS["Lambda_QCD_5flavor"]["value"]

    # Standard QCD
    alpha_qcd = alpha_s_qcd(Q, n_f=n_f, Lambda=Lambda)

    if np.isnan(alpha_qcd):
        return np.nan

    # UET Information correction
    # At high Q: quarks are free, I → 0
    # At low Q: confinement, I → I_scale
    I_Q = I_scale / (1 + Q / Lambda)

    # Combined
    alpha_uet = alpha_qcd * (1 + beta_uet * I_Q)

    return alpha_uet


def alpha_s_uet_v2(Q, beta_uet=0.03, Q0=1.0):
    """
    UET-enhanced QCD running coupling v2.

    Uses logarithmic Information density:
    I(Q) = ln(Q0/Q) for Q < Q0, else 0

    This captures asymptotic freedom naturally.
    """
    n_f = get_n_f(Q)
    Lambda = QCD_PARAMS["Lambda_QCD_5flavor"]["value"]

    # Standard QCD
    alpha_qcd = alpha_s_qcd(Q, n_f=n_f, Lambda=Lambda)

    if np.isnan(alpha_qcd):
        return np.nan

    # UET Information correction (logarithmic)
    if Q < Q0:
        I_Q = np.log(Q0 / Q)
    else:
        I_Q = 0

    return alpha_qcd * (1 + beta_uet * I_Q)


def alpha_s_uet_v3(Q, Lambda_UET=0.25):
    """
    UET-enhanced QCD v3 - Unified formula.

    Uses modified Λ that absorbs UET effects:
    Λ_UET = Λ_QCD × (1 + β_correction)

    This is the cleanest approach that maintains
    proper asymptotic freedom.
    """
    n_f = get_n_f(Q)

    # UET modifies the effective Λ
    # At low Q, Information effects increase confinement scale
    return alpha_s_qcd(Q, n_f=n_f, Lambda=Lambda_UET, order="NNLO")


# ================================================================
# CALIBRATION
# ================================================================


def calibrate_beta_uet():
    """
    Calibrate β_UET by minimizing error against PDG data.
    """
    best_beta = 0
    best_error = float("inf")

    for beta in np.linspace(0, 0.2, 50):
        errors = []
        for Q, alpha_exp, err, method, ref in ALPHA_S_DATA:
            alpha_pred = alpha_s_uet_v1(Q, beta_uet=beta)
            if not np.isnan(alpha_pred):
                error = abs(alpha_pred - alpha_exp) / alpha_exp * 100
                errors.append(error)

        avg_error = np.mean(errors) if errors else float("inf")

        if avg_error < best_error:
            best_error = avg_error
            best_beta = beta

    return best_beta, best_error


def calibrate_lambda():
    """
    Calibrate Λ_UET by minimizing error.
    """
    best_lambda = 0.2
    best_error = float("inf")

    for lam in np.linspace(0.15, 0.35, 50):
        errors = []
        for Q, alpha_exp, err, method, ref in ALPHA_S_DATA:
            alpha_pred = alpha_s_uet_v3(Q, Lambda_UET=lam)
            if not np.isnan(alpha_pred):
                error = abs(alpha_pred - alpha_exp) / alpha_exp * 100
                errors.append(error)

        avg_error = np.mean(errors) if errors else float("inf")

        if avg_error < best_error:
            best_error = avg_error
            best_lambda = lam

    return best_lambda, best_error


# ================================================================
# VALIDATION
# ================================================================


def validate_against_pdg():
    """Compare all models against PDG 2024 data."""
    results = {"qcd_pure": [], "uet_v1": [], "uet_v3": []}

    for Q, alpha_exp, err_exp, method, ref in ALPHA_S_DATA:
        n_f = get_n_f(Q)

        # Pure QCD
        alpha_qcd = alpha_s_qcd(Q, n_f=n_f)
        if not np.isnan(alpha_qcd):
            err = abs(alpha_qcd - alpha_exp) / alpha_exp * 100
            results["qcd_pure"].append(err)

        # UET v1
        alpha_uet1 = alpha_s_uet_v1(Q, beta_uet=0.05)
        if not np.isnan(alpha_uet1):
            err = abs(alpha_uet1 - alpha_exp) / alpha_exp * 100
            results["uet_v1"].append(err)

        # UET v3
        alpha_uet3 = alpha_s_uet_v3(Q, Lambda_UET=0.22)
        if not np.isnan(alpha_uet3):
            err = abs(alpha_uet3 - alpha_exp) / alpha_exp * 100
            results["uet_v3"].append(err)

    return {k: np.mean(v) if v else float("inf") for k, v in results.items()}


if __name__ == "__main__":
    print("=" * 60)
    print("UET-QCD Bridge Model - Calibration")
    print("=" * 60)

    # Calibrate
    print("\nCalibrating β_UET...")
    best_beta, beta_err = calibrate_beta_uet()
    print(f"  Best β_UET = {best_beta:.4f}, Error = {beta_err:.1f}%")

    print("\nCalibrating Λ_UET...")
    best_lambda, lambda_err = calibrate_lambda()
    print(f"  Best Λ_UET = {best_lambda:.4f} GeV, Error = {lambda_err:.1f}%")

    # Validate
    print("\n" + "=" * 60)
    print("Validation against PDG 2024")
    print("=" * 60)

    errors = validate_against_pdg()
    print(f"\n{'Model':<20} {'Avg Error':<15}")
    print("-" * 35)
    for model, err in errors.items():
        print(f"{model:<20} {err:<15.1f}%")

    # Detailed comparison
    print("\n" + "=" * 60)
    print("Detailed Comparison")
    print("=" * 60)
    print(f"\n{'Q (GeV)':<10} {'Exp':<10} {'QCD':<10} {'UET':<10} {'UET Err':<10}")
    print("-" * 55)

    for Q, alpha_exp, err_exp, method, ref in ALPHA_S_DATA[:10]:
        alpha_qcd = alpha_s_qcd(Q, n_f=get_n_f(Q))
        alpha_uet = alpha_s_uet_v3(Q, Lambda_UET=best_lambda)

        if not np.isnan(alpha_uet):
            uet_err = abs(alpha_uet - alpha_exp) / alpha_exp * 100
            print(
                f"{Q:<10.1f} {alpha_exp:<10.4f} {alpha_qcd:<10.4f} {alpha_uet:<10.4f} {uet_err:<10.1f}%"
            )
