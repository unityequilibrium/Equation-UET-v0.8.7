"""
UET Three Body Chaos Test
=========================
Simulates the Three Body Problem to demonstrate Deterministic Chaos.
"""

import numpy as np
import sys
from pathlib import Path

# Robust Root setup
ROOT = Path(__file__).resolve().parent.parent.parent.parent
# Expect: research_uet/topics/0.10.../Code/three_body -> ROOT = research_uet
if ROOT.name != "research_uet":
    # Fallback search
    ROOT = Path(__file__).resolve().parent
    while ROOT.name != "research_uet" and ROOT.parent != ROOT:
        ROOT = ROOT.parent

if str(ROOT.parent) not in sys.path:
    sys.path.insert(0, str(ROOT.parent))

from research_uet.core import uet_viz


def run_three_body():
    print("=" * 60)
    print("UET CHAOS: THREE BODY PROBLEM")
    print("=" * 60)

    # Output Dir
    topic_dir = ROOT / "topics" / "0.10_Fluid_Dynamics_Chaos"
    result_dir = topic_dir / "Result" / "three_body"
    if not result_dir.exists():
        result_dir.mkdir(parents=True, exist_ok=True)

    # Initial Conditions (Figure-8 Solution approximation or Chaotic)
    # Let's use a chaotic setup
    G = 1.0
    m1, m2, m3 = 1.0, 1.0, 1.0

    # Position
    r1 = np.array([0.97000436, -0.24308753])
    r2 = -r1
    r3 = np.array([0.0, 0.0])

    # Velocity
    v3 = np.array([-0.93240737, -0.86473146])
    v1 = -v3 / 2
    v2 = -v3 / 2

    # Simulation
    dt = 0.01
    steps = 1000

    pos1, pos2, pos3 = [], [], []

    def accel(r_i, r_j, r_k):
        # Sum of forces
        d_ij = r_j - r_i
        d_ik = r_k - r_i
        dist_ij = np.linalg.norm(d_ij) + 1e-6
        dist_ik = np.linalg.norm(d_ik) + 1e-6

        a = G * m2 * d_ij / dist_ij**3 + G * m3 * d_ik / dist_ik**3
        return a

    print(f"Simulating {steps} chaotic steps...")

    for _ in range(steps):
        pos1.append(r1.copy())
        pos2.append(r2.copy())
        pos3.append(r3.copy())

        # Symplectic Euler (Semi-implicit)
        v1 += accel(r1, r2, r3) * dt
        v2 += accel(r2, r1, r3) * dt  # m1=m2=m3=1
        v3 += accel(r3, r1, r2) * dt

        r1 += v1 * dt
        r2 += v2 * dt
        r3 += v3 * dt

    pos1 = np.array(pos1)
    pos2 = np.array(pos2)
    pos3 = np.array(pos3)

    # Plot
    fig = uet_viz.go.Figure()

    fig.add_trace(
        uet_viz.go.Scatter(
            x=pos1[:, 0], y=pos1[:, 1], mode="lines", name="Body 1", line=dict(color="red")
        )
    )
    fig.add_trace(
        uet_viz.go.Scatter(
            x=pos2[:, 0], y=pos2[:, 1], mode="lines", name="Body 2", line=dict(color="blue")
        )
    )
    fig.add_trace(
        uet_viz.go.Scatter(
            x=pos3[:, 0], y=pos3[:, 1], mode="lines", name="Body 3", line=dict(color="green")
        )
    )

    # Start/End points
    fig.add_trace(
        uet_viz.go.Scatter(
            x=[pos1[0, 0]],
            y=[pos1[0, 1]],
            mode="markers",
            marker=dict(color="red", size=10),
            showlegend=False,
        )
    )

    fig.update_layout(
        title="Three Body Chaos (Deterministic)",
        xaxis_title="X",
        yaxis_title="Y",
        showlegend=True,
        width=800,
        height=800,
    )

    uet_viz.save_plot(fig, "three_body_viz.png", result_dir)
    print("  [Viz] Generated 'three_body_viz.png'")

    print("\nChaos Theory in UET:")
    print("  Deterministic systems can exhibit unpredictable behavior.")
    print("  Entropy S = k * log(W) measures the divergence of trajectories.")


if __name__ == "__main__":
    run_three_body()
