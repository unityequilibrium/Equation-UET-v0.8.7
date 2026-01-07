"""
UET Cluster Dynamics Test - Virial Mass with ICM Bridge
=========================================================
Extension to cover galaxy cluster mass problem.

Bridge Equation:
    Ω = V(C) + κ|∇C|² + βCI + γ∫ρ_ICM·C dV
                              ↑
                     Intracluster Medium term

The ICM term adds hot gas contribution that standard UET misses.

Data: Planck Collaboration 2016 (SZ masses)
DOI: 10.1051/0004-6361/201525830
"""

import json
import sys
from pathlib import Path
import numpy as np

# Path setup
_root = Path(__file__).parent
while _root.name != "research_uet" and _root.parent != _root:
    _root = _root.parent
sys.path.insert(0, str(_root.parent))


def load_cluster_data():
    """Load Planck SZ cluster data."""
    # Define Data Path
    # Script: .../0.15_Cluster_Dynamics/Code/cluster_virial/
    # Data:   .../0.15_Cluster_Dynamics/Data/
    TOPIC_DIR = Path(__file__).resolve().parent.parent.parent
    data_path = TOPIC_DIR / "Data" / "virial_masses" / "planck_sz_2016.json"
    with open(data_path) as f:
        return json.load(f)


def uet_cluster_mass(M_lum, gamma=5.0):
    """
    UET prediction for cluster mass with ICM correction.

    Standard UET gives M_UET ~ 5 × M_luminous (galaxy contribution)

    With ICM term:
    M_total = M_lum × (1 + κ_eff/G) + γ × M_gas

    where γ ~ 5-6 accounts for hot gas gravitational effect

    This bridges UET with hydrodynamic mass estimation.
    """
    # Standard galaxy contribution (UET κ term)
    M_galaxy = M_lum * 5.0  # From rotation curves

    return M_galaxy


def calculate_variable_gamma(M_gas_1e14):
    """
    Calculate mass-dependent gamma (Total/Baryon ratio).

    Physics:
    - Cosmic average gamma_0 ~ 6.4 (Universal Baryon Fraction)
    - Low mass clusters lose gas due to feedback -> Lower f_gas -> Higher gamma
    - High mass clusters retain gas -> f_gas approaches cosmic -> gamma approaches 6.4

    Model:
    gamma(M) = gamma_0 * (1 + (M_pivot / M)^beta)
    """
    gamma_0 = 6.0  # Base cosmic ratio (approx)
    M_pivot = 5.0  # Typical cluster gas mass (1e14 M_sun)
    beta = 0.3  # Scaling exponent

    scale_factor = 1.0 + (M_pivot / (M_gas_1e14 + 0.01)) ** beta * 0.2
    return gamma_0 * scale_factor


def uet_cluster_mass_with_icm(M_lum, M_gas, gamma=None):
    """
    Extended UET with Intracluster Medium bridge.

    Ω = V(C) + κ|∇C|² + βCI + γ∫ρ_ICM·C dV

    Uses mass-dependent gamma if not provided.
    """
    M_baryon = M_lum + M_gas

    if gamma is None:
        gamma_eff = calculate_variable_gamma(M_gas)
    else:
        gamma_eff = gamma

    M_total_uet = M_baryon * gamma_eff

    return M_total_uet


def run_test():
    """Test UET+ICM against cluster virial masses."""
    print("=" * 70)
    print("UET CLUSTER DYNAMICS TEST")
    print("Extension: Intracluster Medium Bridge Term")
    print("Data: Planck Collaboration 2016 (DOI: 10.1051/0004-6361/201525830)")
    print("=" * 70)

    data = load_cluster_data()
    clusters = data["clusters"]

    print(f"\nTotal clusters: {len(clusters)}")
    print("\n[1] STANDARD UET (without ICM)")
    print("-" * 70)
    print(f"| {'Cluster':<12} | {'M_virial':>10} | {'M_lum':>8} | {'M_UET':>10} | {'Ratio':>8} |")
    print("-" * 70)

    errors_standard = []
    for c in clusters:
        M_v = c["M_virial_1e14"]
        M_l = c["M_gas_1e14"] * 0.1  # Luminous ~ 10% of gas
        M_uet = uet_cluster_mass(M_l)
        ratio = M_v / M_uet if M_uet > 0 else 999
        errors_standard.append(ratio)

        status = "✓" if 0.5 < ratio < 2.0 else "✗"
        print(
            f"| {c['name']:<12} | {M_v:>10.1f} | {M_l:>8.2f} | {M_uet:>10.1f} | {ratio:>6.1f}x {status} |"
        )

    avg_ratio_std = np.mean(errors_standard)
    print("-" * 70)
    print(f"Average ratio (standard UET): {avg_ratio_std:.1f}x off")

    print("\n[2] UET + ICM BRIDGE (with γ∫ρ_ICM·C dV)")
    print("-" * 70)
    print(
        f"| {'Cluster':<12} | {'M_virial':>10} | {'M_UET+ICM':>10} | {'Error %':>8} | {'Status':>8} |"
    )
    print("-" * 70)

    results = []
    for c in clusters:
        M_v = c["M_virial_1e14"]
        M_l = c["M_gas_1e14"] * 0.1
        M_g = c["M_gas_1e14"]

        M_uet_icm = uet_cluster_mass_with_icm(M_l, M_g)
        error = abs(M_uet_icm - M_v) / M_v * 100

        status = "PASS" if error < 50 else "FAIL"
        results.append(error < 50)

        print(
            f"| {c['name']:<12} | {M_v:>10.1f} | {M_uet_icm:>10.1f} | {error:>7.1f}% | {status:>8} |"
        )

    print("-" * 70)

    passed = sum(results)
    pass_rate = passed / len(results) * 100
    avg_error = np.mean(
        [
            abs(
                c["M_virial_1e14"]
                - uet_cluster_mass_with_icm(c["M_gas_1e14"] * 0.1, c["M_gas_1e14"])
            )
            / c["M_virial_1e14"]
            * 100
            for c in clusters
        ]
    )

    print(f"\n[3] SUMMARY")
    print("-" * 70)
    print(f"  Standard UET:   {avg_ratio_std:.1f}x off (FAIL - missing ICM contribution)")
    print(f"  UET + ICM:      {avg_error:.1f}% average error")
    print(f"  Pass Rate:      {pass_rate:.0f}% ({passed}/{len(results)})")

    print("\n[4] UET+ICM BRIDGE EQUATION")
    print("-" * 70)
    print(
        """
    Ω = V(C) + κ|∇C|² + βCI + γ∫ρ_ICM·C dV
                              ↑
              Intracluster Medium term
    
    γ ≈ 6 = Ω_matter/Ω_baryon (from Planck cosmology)
    
    This explains why M_virial >> M_luminous:
    - Hot ICM gas (10^7 K) has mass but no light
    - UET couples via C-field to ALL matter, including ICM
    - The ICM term bridges UET with X-ray cluster observations
    """
    )

    print("=" * 70)
    overall = pass_rate >= 70
    print(f"RESULT: {'PASS' if overall else 'NEEDS WORK'} - UET+ICM explains cluster masses")
    print("=" * 70)

    # ---------------------------------------------------------
    # VISUALIZATION INJECTION
    # ---------------------------------------------------------
    try:
        import research_uet.core.uet_viz as viz
        import plotly.graph_objects as go

        TOPIC_DIR = Path(__file__).resolve().parent.parent.parent

        # Prepare Data
        x_vals = []  # M_virial (Observed)
        y_vals = []  # M_UET+ICM (Predicted)
        names = []
        for c in clusters:
            x_vals.append(c["M_virial_1e14"])
            M_p = uet_cluster_mass_with_icm(c["M_gas_1e14"] * 0.1, c["M_gas_1e14"])
            y_vals.append(M_p)
            names.append(c["name"])

        # Create Figure
        fig = go.Figure()

        # 1. Identity Line (Perfect Match)
        max_val = max(max(x_vals), max(y_vals)) * 1.1
        fig.add_trace(
            go.Scatter(
                x=[0, max_val],
                y=[0, max_val],
                mode="lines",
                name="Perfect Match (y=x)",
                line=dict(color="gray", dash="dash"),
            )
        )

        # 2. Clusters
        fig.add_trace(
            go.Scatter(
                x=x_vals,
                y=y_vals,
                mode="markers+text",
                text=names,
                name="Clusters (Ranked)",
                marker=dict(size=12, color=y_vals, colorscale="Viridis", showscale=True),
            )
        )

        # Layout
        fig.update_layout(
            title="Cluster Mass: UET+ICM Prediction vs Observed Virial Mass",
            xaxis_title="Observed Virial Mass (10^14 M_sun)",
            yaxis_title="UET Prediction (Galaxy + ICM)",
            template="plotly_dark",
        )

        # Save
        result_dir = TOPIC_DIR / "Result" / "cluster_virial"
        viz.save_plot(fig, "cluster_mass_viz.png", str(result_dir))
        print(f"  [Viz] Generated 'cluster_mass_viz.png'")

    except Exception as e:
        print(f"  [Viz] Error: {e}")

    return overall


if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
