"""
UET Galaxy Comparison: Spiral vs Compact
========================================
Visualizes the UET prediction curve vs the Observed Data Point.

Target Galaxies from SPARC_GALAXIES (test_175_galaxies.py):
1. Spiral: NGC3198 (Classic Success)
2. Compact: NGC4736 (Classic Failure)
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from test_175_galaxies import uet_rotation_velocity, SPARC_GALAXIES


def get_galaxy(name_target):
    for g in SPARC_GALAXIES:
        if g[0] == name_target:
            return g
    return None


def run_comparison():
    # Setup Output
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "outputs",
        "galaxies",
    )
    os.makedirs(output_dir, exist_ok=True)

    # 1. Select Galaxies
    spiral = get_galaxy("NGC3198")
    compact = get_galaxy("NGC4736")

    if not spiral or not compact:
        print("Error: Could not find target galaxies in SPARC_GALAXIES list.")
        return

    galaxies = [spiral, compact]
    titles = ["Spiral (Low Conflict)", "Compact (High Conflict)"]

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    for ax, gal, title in zip(axes, galaxies, titles):
        name, R_opt, v_obs, M_disk, R_disk, gtype = gal

        # Determine Plot Range (0 to 1.5 * R_opt)
        r_range = np.linspace(0.1, R_opt * 1.5, 100)

        # Calculate Prediction Curve
        v_preds = []
        for r in r_range:
            v = uet_rotation_velocity(r, M_disk, R_disk, gtype)
            v_preds.append(v)

        # Plot Prediction
        ax.plot(r_range, v_preds, "b-", linewidth=2, label="UET Prediction")

        # Plot Observation (The single point used for audit)
        ax.plot(R_opt, v_obs, "ro", markersize=8, label=f"Observed ({v_obs} km/s)")
        # Draw "observed" flat line approximation for context
        ax.axhline(v_obs, color="gray", linestyle="--", alpha=0.5, label="Approx Flat V")

        # Calculate Error
        v_at_opt = uet_rotation_velocity(R_opt, M_disk, R_disk, gtype)
        error = abs(v_at_opt - v_obs) / v_obs * 100

        # Styling
        status = "PASS" if error < 15 else "FAIL"
        color = "green" if status == "PASS" else "red"

        ax.set_title(f"{name} ({gtype})\nError: {error:.1f}% ({status})", fontsize=14, color=color)
        ax.set_xlabel("Radius (kpc)")
        ax.set_ylabel("Velocity (km/s)")
        ax.grid(True, alpha=0.3)
        ax.legend()

        # Game Theory Annotation
        if gtype == "compact":
            ax.text(
                0.5,
                0.4,
                "High Density = High Conflict\nMissing 'Efficiency' Term",
                transform=ax.transAxes,
                ha="center",
                color="red",
                fontsize=10,
                bbox=dict(facecolor="white", edgecolor="red", alpha=0.8),
            )

    plt.suptitle("UET Validation: Success vs Failure Modes", fontsize=16)

    output_path = os.path.join(output_dir, "spiral_vs_compact.png")
    plt.savefig(output_path)
    print(f"Chart saved to: {output_path}")


if __name__ == "__main__":
    run_comparison()
