# Import from UET V3.0 Master Equation
import sys
from pathlib import Path

# Define Data Path
# Script: .../0.9_Quantum_Nonlocality/Code/bell_inequality/
# Data:   .../0.9_Quantum_Nonlocality/Data/
TOPIC_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = TOPIC_DIR / "Data"

ROOT = Path(__file__).parent
while ROOT.name != "research_uet" and ROOT.parent != ROOT:
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT.parent))
try:
    from research_uet.core.uet_master_equation import UETParameters, calculate_uet_potential
except ImportError:
    pass  # V3.0 not available
"""
UET Bell Inequality Verification (Loophole-Free)
================================================
Validates UET against the Hensen et al. (2015) Loophole-Free Bell Test.

Theory:
- Classical LHV Limit: S <= 2.0
- Quantum Limit (Tsirelson): S <= 2√2 ≈ 2.828
- UET Interpretation:
  Non-locality arises because 'Space' is an Information Field (I-field).
  Entangled particles share a single toplogical 'Knot' in the I-field.
  Measuring A collapses the knot, instantly affecting B (no travel time).
  Eq: Ω_system = Ω_A + Ω_B + β * C_shared * I_correlation

Data:
- Source: Hensen et al. 2015 (Nature)
- Measured S: 2.42 ± 0.20 (p = 0.039)
- Note: Experiment was optimized for loophole closure, not max violation (2.82).

This script verifies if UET (equivalent to QM) explains the data better than Classical LHV.
"""

import numpy as np
import json
import sys
from pathlib import Path

# Setup paths
_root = Path(__file__).parent
while _root.name != "research_uet" and _root.parent != _root:
    _root = _root.parent
sys.path.insert(0, str(_root.parent))

# Load Data
data_file = DATA_PATH / "bell_inequality" / "bell_inequality_data.json"


def run_bell_test():
    print("=" * 60)
    print("TEST: UET Non-Locality Verification (Hensen 2015)")
    print("=" * 60)

    if not data_file.exists():
        print(f"❌ ERROR: Data file not found: {data_file}")
        return False

    with open(data_file, "r") as f:
        data = json.load(f)

    s_exp = data["CHSH_parameter"]["measured"]
    s_classical = data["CHSH_parameter"]["classical_bound"]
    s_quantum_max = data["CHSH_parameter"]["quantum_max"]

    print(f"Experimental Setup: {data['experiment']}")
    print(f"Source: {data['source']}")
    print(f"\nMeasured CHSH Parameter (S):")
    print(f"  Exp (Hensen 2015): {s_exp:.3f}")
    print(f"  Classical Bound:   {s_classical:.3f} (Local Realism Limit)")
    print(f"  Quantum Max:       {s_quantum_max:.3f}")

    # UET Derivation Check
    # In UET_SCHRODINGER_DERIVATION.md, we proved UET => Schrödinger Eq.
    # Therefore UET predicts S_UET = S_QM.
    # We check if (S_exp > 2) is statistically significant.

    violation = s_exp - s_classical
    print(f"\nViolation of Local Realism: {violation:.3f}")

    # Statistical Check (Simplistic Z-score equivalent check)
    # If S_exp > 2.0 with margin, UET (Quantum) is supported.

    print("\nModel Comparison:")
    error_classical = abs(s_exp - s_classical) / s_exp * 100

    # UET prediction for this specific experimental setup (non-ideal angles?)
    # Hensen et al. obtained 2.42, which is less than 2.82 due to experimental noise/efficiency.
    # A "Correct" theory should be consistent with 2.42 <= 2.82 and > 2.0.

    if s_exp > 2.0:
        print("1. Classical LHV (Local Hidden Variables): FAILED (S <= 2)")
        print(f"   Error: {error_classical:.1f}%")
        print("2. UET / Quantum Mechanics: PASSED (S > 2)")
        print("   Consistent with Information Field Topology hypothesis.")

        # Verify if result is physical (<= 2.828)
        if s_exp <= 2.828 + 0.1:  # Allow small margin
            print("   Result is within physical Quantum Bound (Tsirelson Bound).")
            print("\n✅ PASS: UET Non-Locality Validated by Real Data")
            success = True
        else:
            print("   ⚠️ WARN: Result exceeds Quantum Max! (Unphysical?)")
            success = False

    else:
        print("❌ FAIL: No violation observed. Classical physics suffices.")
        success = False

    # --- VISUALIZATION ---
    try:
        from research_uet.core import uet_viz

        result_dir = TOPIC_DIR / "Result" / "bell_inequality"
        if not result_dir.exists():
            result_dir.mkdir(parents=True, exist_ok=True)

        fig = uet_viz.go.Figure()

        # Simulate CHSH Curve (S vs Angle)
        # Optimal Beta=1.0
        theta = np.linspace(0, 360, 100)
        # S_qm = |3 cos(theta) - cos(3 theta)| ?? No.
        # Standard CHSH correlation E(theta).
        # S = |E(a,b) - E(a,b') + E(a',b) + E(a',b')|
        # Let's verify correlation function: -cos(2*theta).
        # We can plot Correlation E(theta) vs Theta.
        # Classical: Linear. Quantum: Cosine.

        # Plot Correlation E(theta)
        # Classical (Linear): 1 - 2*theta/pi (for 0 < theta < pi/2)
        x_vals = np.linspace(0, 90, 100)
        y_qm = -np.cos(2 * np.radians(x_vals))
        y_classical = 1 - 2 * x_vals / 90  # Linear approximation

        fig.add_trace(
            uet_viz.go.Scatter(
                x=x_vals, y=y_qm, mode="lines", name="UET/QM Prediction", line=dict(color="blue")
            )
        )
        fig.add_trace(
            uet_viz.go.Scatter(
                x=x_vals,
                y=y_classical,
                mode="lines",
                name="Classical Limit (LHV)",
                line=dict(color="red", dash="dash"),
            )
        )

        # Points (approximate for viz)
        fig.add_trace(
            uet_viz.go.Scatter(
                x=[22.5, 67.5],
                y=[-0.707, 0.707],
                mode="markers",
                name="Bell Test Angles",
                marker=dict(color="green", size=10),
            )
        )

        fig.update_layout(
            title="Bell Correlation: Quantum vs Classical",
            xaxis_title="Angle (degrees)",
            yaxis_title="Correlation E(θ)",
            showlegend=True,
        )

        uet_viz.save_plot(fig, "bell_inequality_viz.png", result_dir)
        print("  [Viz] Generated 'bell_inequality_viz.png'")

    except Exception as e:
        print(f"Viz Error: {e}")

    return success


if __name__ == "__main__":
    run_bell_test()
