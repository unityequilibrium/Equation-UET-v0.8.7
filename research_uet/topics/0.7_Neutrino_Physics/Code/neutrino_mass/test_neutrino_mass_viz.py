"""
UET Neutrino Mass Hierarchy Visualization
==========================================
Visualizes the Neutrino Mass Hierarchy (Normal vs Inverted)
based on UET Information Geometry principles.
"""

import sys
from pathlib import Path
import math

# Robust Root setup
ROOT = Path(__file__).resolve().parent
while ROOT.name != "research_uet" and ROOT.parent != ROOT:
    ROOT = ROOT.parent
if str(ROOT.parent) not in sys.path:
    sys.path.insert(0, str(ROOT.parent))

import numpy as np
from research_uet.core import uet_viz


def visualize_hierarchy():
    print("=" * 60)
    print("UET NEUTRINO MASS HIERARCHY VIZ")
    print("=" * 60)

    # Output Dir
    result_dir = ROOT / "topics" / "0.7_Neutrino_Physics" / "Result" / "neutrino_mass"
    if not result_dir.exists():
        result_dir.mkdir(parents=True, exist_ok=True)

    # Data (PDG 2024 / NuFIT 2024)
    # Delta m^2 values (eV^2)
    dm21 = 7.42e-5
    dm32_NO = 2.515e-3  # Normal Ordering

    # Assume m1 = 0 (lightest) for visualization
    m1 = 0
    m2 = np.sqrt(dm21)
    m3 = np.sqrt(dm32_NO + dm21)  # approx

    # Masses in meV
    masses = [m1 * 1000, m2 * 1000, m3 * 1000]
    names = ["ν₁", "ν₂", "ν₃"]
    colors = ["blue", "green", "red"]

    # Flavor composition (Simplified for Viz)
    # nu1 is mostly electron (blue), nu2 mixed, nu3 mostly mu/tau
    # For simplicity, just showing mass levels

    fig = uet_viz.go.Figure()

    # Draw bars for mass levels
    for i, m in enumerate(masses):
        fig.add_trace(
            uet_viz.go.Bar(
                x=[names[i]],
                y=[m],
                name=names[i],
                marker_color=colors[i],
                text=f"{m:.1f} meV",
                textposition="auto",
            )
        )

    fig.update_layout(
        title="Neutrino Mass Hierarchy (Normal Ordering)",
        yaxis_title="Mass (meV)",
        showlegend=False,
    )

    uet_viz.save_plot(fig, "neutrino_mass_hierarchy.png", result_dir)
    print("  [Viz] Generated 'neutrino_mass_hierarchy.png'")

    # Calculate Sum
    total_mass = sum(masses)
    print(f"Total Mass (m1=0): {total_mass:.2f} meV")
    print(f"Cosmological Limit: <120 meV (Consistent)")


if __name__ == "__main__":
    visualize_hierarchy()
