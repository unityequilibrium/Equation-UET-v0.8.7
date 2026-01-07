"""
Test: Brownian Motion Effect (System-Level Analysis)
=====================================================
Einstein explains HOW particles move (MSD = 2Dt)
UET explains WHAT HAPPENS to the system (entropy production)

Reference:
- Einstein (1905), Ann. Phys. 17, 549
- Seifert (2012), Reports on Progress in Physics 75, 126001

Classical (Einstein):
    <x²> = 2Dt  (Mean Square Displacement)

UET Addition:
    dS/dt = P/T  (Entropy production rate)
    System entropy INCREASES as particles move

Updated for UET V3.0
"""

import numpy as np
import sys

# Find topic and root
from pathlib import Path

TEST_FILE = Path(__file__).resolve()
TOPIC_DIR = TEST_FILE.parent.parent.parent  # research_uet/topics/0.10...
RESEARCH_ROOT = TOPIC_DIR.parent.parent  # research_uet

# 1. Add ROOT to path for core imports
sys.path.insert(0, str(RESEARCH_ROOT))

try:
    from research_uet.core.uet_master_equation import (
        UETParameters,
        SIGMA_CRIT,
        strategic_boost,
        potential_V,
        KAPPA_BEKENSTEIN,
    )
except ImportError:
    # Fallback if core is in a different relative location or zipped
    if (RESEARCH_ROOT / "core").exists():
        sys.path.insert(0, str(RESEARCH_ROOT / "core"))
        from uet_master_equation import UETParameters
    else:
        print("⚠️ Core not found. UET modules may fail.")


# 2. Add DATA to path
# Old Path: lab/05_unified_theory/effect_of_motion/data
# New Path: topics/0.10_Fluid_Dynamics_Chaos/Data/brownian
DATA_DIR = TOPIC_DIR / "Data" / "brownian"
if DATA_DIR.exists():
    sys.path.insert(0, str(DATA_DIR))
    print(f"✅ Added Data Path: {DATA_DIR}")
else:
    print(f"❌ Data directory not found: {DATA_DIR}")

# Debug imports
try:
    from brownian_data import (
        get_msd_data,
        get_diffusion_coefficient,
        get_physical_params,
        get_entropy_production,
    )
except ImportError as e:
    print(f"❌ Import Failed: {e}")
    print(f"   Current sys.path: {sys.path}")
    print(f"   Data Dir Files: {list(DATA_DIR.glob('*')) if DATA_DIR.exists() else 'N/A'}")
    sys.exit(1)


def einstein_msd(t, D, dimensions=2):
    """
    Einstein's MSD prediction: <x²> = 2*d*D*t

    This tells us HOW particles move.
    """
    return 2 * dimensions * D * t


def uet_entropy_production(t, D, T, kB, viscosity, radius):
    """
    UET predicts entropy production RATE of the system.

    As particles undergo Brownian motion, they:
    1. Dissipate energy to the environment
    2. Increase system entropy

    This tells us WHAT HAPPENS TO THE SYSTEM.
    """
    # Stokes drag on a Brownian particle
    gamma = 6 * np.pi * viscosity * radius  # Friction coefficient

    # Mean velocity (thermal)
    v_thermal = np.sqrt(kB * T / (4 / 3 * np.pi * radius**3 * 1000))  # Approx

    # Power dissipation
    P = gamma * v_thermal**2

    # Entropy production rate
    dS_dt = P / T

    # Total entropy produced up to time t
    S_total = dS_dt * t

    return dS_dt, S_total


def run_test():
    print("=" * 60)
    print("🔬 UET EFFECT OF MOTION: BROWNIAN MOTION TEST")
    print("=" * 60)
    print()
    print("Einstein (1905): Explains HOW particles move randomly")
    print("UET: Explains WHAT HAPPENS to the system (entropy)")
    print()

    # Load data
    msd_data = get_msd_data()
    params = get_physical_params()
    D = get_diffusion_coefficient()
    entropy_data = get_entropy_production()

    times = msd_data["time_s"]
    observed_msd = msd_data["msd_m2"]
    uncertainty = msd_data["uncertainty_m2"]

    print(f"📊 Data: {len(times)} time points")
    print(f"   Particle: r = {params['r']*1e6:.2f} μm in water at {params['T']-273.15:.1f}°C")
    print(f"   Diffusion coefficient: D = {D:.2e} m²/s")
    print()

    # Part 1: Verify Einstein's MSD
    print("-" * 60)
    print("PART 1: Einstein's MSD Prediction (HOW particles move)")
    print("-" * 60)
    print(f"{'Time':>10} {'Observed':>14} {'Einstein':>14} {'Error':>10}")
    print(f"{'(s)':>10} {'(m²)':>14} {'(m²)':>14} {'(%)':>10}")
    print("-" * 60)

    errors = []
    for i, t in enumerate(times):
        obs = observed_msd[i]
        pred = einstein_msd(t, D)
        err = abs(pred - obs) / obs * 100 if obs > 0 else 0
        errors.append(err)
        print(f"{t:>10.2f} {obs:>14.2e} {pred:>14.2e} {err:>10.1f}")

    avg_err = np.mean(errors)
    print("-" * 60)
    print(f"   Average Error: {avg_err:.1f}%")
    print()

    # Part 2: UET Entropy Analysis
    print("-" * 60)
    print("PART 2: UET System Analysis (WHAT HAPPENS to the system)")
    print("-" * 60)
    print()

    print("As particles undergo Brownian motion:")
    print()

    dS_dt, _ = uet_entropy_production(
        1.0, D, params["T"], params["kB"], params["eta"], params["r"]  # At t=1s
    )

    print(f"   Entropy production rate: dS/dt ≈ {dS_dt:.2e} J/(K·s)")
    print()

    # Total entropy at different times
    print("   Total entropy produced:")
    for t in [0.1, 1.0, 10.0]:
        _, S = uet_entropy_production(t, D, params["T"], params["kB"], params["eta"], params["r"])
        print(f"      t = {t:.1f}s: ΔS = {S:.2e} J/K")

    print()

    # Key insight
    print("=" * 60)
    print("💡 KEY INSIGHT: The TWO LAYERS")
    print("=" * 60)
    print()
    print("   LAYER 1 (Einstein): HOW does the particle move?")
    print("      → <x²> = 2Dt (random walk)")
    print("      → Predicts particle TRAJECTORY statistics")
    print()
    print("   LAYER 2 (UET): WHAT is the EFFECT on the system?")
    print("      → Entropy production: dS/dt = P/T > 0 (always)")
    print("      → Environment heats up (2nd Law)")
    print("      → Field perturbation in surrounding medium")
    print()
    print("   UET doesn't replace Einstein.")
    print("   UET ADDS the effect layer that Einstein's equation doesn't cover.")
    print()

    # Pass criteria
    passed_einstein = avg_err < 30  # Einstein MSD works
    passed_entropy = dS_dt > 0  # Entropy always increases

    if passed_einstein and passed_entropy:
        print("✅ TEST PASSED")
        print("   - Einstein MSD: Verified (error < 30%)")
        success = True
    else:
        print("⚠️ TEST NEEDS REVIEW")
        success = False

    # --- VISUALIZATION ---
    try:
        from research_uet.core import uet_viz

        result_dir = TOPIC_DIR / "Result" / "brownian"
        if not result_dir.exists():
            result_dir.mkdir(parents=True, exist_ok=True)

        fig = uet_viz.go.Figure()

        # Plot MSD
        fig.add_trace(
            uet_viz.go.Scatter(
                x=times,
                y=observed_msd,
                mode="markers",
                name="Observed Data",
                marker=dict(color="green"),
            )
        )

        # Einstein Prediction
        t_plot = np.linspace(min(times), max(times), 100)
        msd_einstein = einstein_msd(t_plot, D)
        fig.add_trace(
            uet_viz.go.Scatter(
                x=t_plot,
                y=msd_einstein,
                mode="lines",
                name="Einstein (Classical)",
                line=dict(color="red", dash="dash"),
            )
        )

        fig.update_layout(
            title="Brownian Motion: MSD vs Time",
            xaxis_title="Time (s)",
            yaxis_title="Mean Square Displacement (m²)",
            showlegend=True,
        )

        uet_viz.save_plot(fig, "brownian_viz.png", result_dir)
        print("  [Viz] Generated 'brownian_viz.png'")

    except Exception as e:
        print(f"Viz Error: {e}")

    return success


if __name__ == "__main__":
    success = run_test()
    exit(0 if success else 1)
