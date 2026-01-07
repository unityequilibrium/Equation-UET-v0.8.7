"""
UET Double Slit Interference Test
=================================
Visualizes the Double Slit Interference Pattern predicted by UET (Pilot Wave).
"""

import numpy as np
import sys
from pathlib import Path

# Robust Root setup
ROOT = Path(__file__).resolve().parent
while ROOT.name != "research_uet" and ROOT.parent != ROOT:
    ROOT = ROOT.parent
if str(ROOT.parent) not in sys.path:
    sys.path.insert(0, str(ROOT.parent))

from research_uet.core import uet_viz


def run_double_slit():
    print("=" * 60)
    print("UET DOUBLE SLIT INTERFERENCE")
    print("=" * 60)

    # Output Dir
    topic_dir = ROOT / "topics" / "0.9_Quantum_Nonlocality"
    result_dir = topic_dir / "Result" / "double_slit"
    if not result_dir.exists():
        result_dir.mkdir(parents=True, exist_ok=True)

    # Simulation Parameters
    x = np.linspace(-10, 10, 500)
    slit_dist = 2.0
    slit_width = 0.5
    wavelength = 1.0
    L = 10.0  # Distance to screen

    # UET/QM Prediction (Interference)
    # Intensity ~ cos^2(pi * d * sin(theta) / lambda) * sinc^2(...)
    theta = np.arctan(x / L)
    # Phase difference
    beta = np.pi * slit_dist * np.sin(theta) / wavelength
    # Diffraction envelope
    alpha = np.pi * slit_width * np.sin(theta) / wavelength

    intensity = (np.cos(beta) ** 2) * (np.sinc(alpha / np.pi) ** 2)

    # Classical (Particle) Prediction: Sum of two Gaussians
    I1 = np.exp(-((x - slit_dist / 2) ** 2) / 0.5)
    I2 = np.exp(-((x + slit_dist / 2) ** 2) / 0.5)
    intensity_cl = I1 + I2

    # Plot
    fig = uet_viz.go.Figure()

    fig.add_trace(
        uet_viz.go.Scatter(
            x=x,
            y=intensity,
            mode="lines",
            name="UET/QM Prediction (Wave)",
            line=dict(color="blue", width=3),
        )
    )

    fig.add_trace(
        uet_viz.go.Scatter(
            x=x,
            y=intensity_cl,
            mode="lines",
            name="Classical Particle (No Interference)",
            line=dict(color="red", dash="dash"),
        )
    )

    fig.update_layout(
        title="Double Slit Experiment: Wave vs Particle",
        xaxis_title="Screen Position (x)",
        yaxis_title="Intensity",
        showlegend=True,
    )

    uet_viz.save_plot(fig, "double_slit_viz.png", result_dir)
    print("  [Viz] Generated 'double_slit_viz.png'")


if __name__ == "__main__":
    run_double_slit()
