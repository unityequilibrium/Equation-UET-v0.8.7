"""
🌌 UET Universe Simulation (Hybrid Engine)
=======================================
Runs a "Whole System" simulation using the stabilized UET 4D Phase Field Engine.
Demonstrates:
1. Baryonic Matter (C-Field) initialized with DC14 Profile (Dwarf Galaxy).
2. Dark Matter (I-Field) initialized with UDL Halo.
3. Stable Evolution via Relaxation Dynamics.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from research_uet.engine.uet_4d_engine import UET4DSolver


def plot_slice(C, I, t, filename):
    """Plot a 2D slice of the 3D fields."""
    z_idx = C.shape[2] // 2

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Plot Baryons (C)
    im1 = axes[0].imshow(C[:, :, z_idx].T, origin="lower", cmap="plasma", vmin=-1.0, vmax=2.0)
    axes[0].set_title(f"Baryonic Matter (C-Field) t={t:.3f}")
    plt.colorbar(im1, ax=axes[0])

    # Plot Information/Dark Matter (I)
    im2 = axes[1].imshow(I[:, :, z_idx].T, origin="lower", cmap="viridis")
    axes[1].set_title(f"Information/Dark Matter (I-Field) t={t:.3f}")
    plt.colorbar(im2, ax=axes[1])

    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"   📸 Saved snapshot: {filename}")


def run_simulation():
    print("=" * 60)
    print("🚀 UET UNIVERSE SIMULATION: DWARF GALAXY EVOLUTION")
    print("=" * 60)

    # 1. Setup Solver (Hybrid Engine Standard Parameters)
    # Using dt=0.0001 for guaranteed stability
    solver = UET4DSolver(
        Nx=64, Ny=64, Nz=64, Lx=20.0, Ly=20.0, Lz=20.0, dt=0.0001, kappa=0.5, beta=0.3
    )

    # 2. Initialize with Analytical DC14 Profile (Research Finding)
    print("\n🌌 Initializing Galaxy (DC14 Profile)...")
    C0, I0 = solver.create_galaxy_initial_condition(
        type="dwarf_galaxy", radius=4.0, core_density=1.5, halo_density=0.5
    )

    # Create output directory
    output_dir = "research_uet/simulation_outputs/dwarf_galaxy_run"
    os.makedirs(output_dir, exist_ok=True)

    # Save Initial State
    plot_slice(C0, I0, 0.0, f"{output_dir}/step_0000.png")

    # 3. Run Evolution
    print("\n🔄 Evolving System...")
    C, I = C0.copy(), I0.copy()

    n_steps = 2000  # 2000 steps * 0.0001 dt = 0.2 time units
    save_interval = 500

    history_file = open(f"{output_dir}/history.txt", "w")
    history_file.write("Step,Time,Energy,MeanC,MeanI\n")

    for step in range(1, n_steps + 1):
        C, I = solver.evolve_step(C, I, evolve_I=True)

        if step % 100 == 0:
            E = solver.compute_energy(C, I)
            t = step * solver.dt
            print(f"   Step {step}: E={E:.5f}")
            history_file.write(f"{step},{t},{E},{np.mean(C)},{np.mean(I)}\n")

        if step % save_interval == 0:
            plot_slice(C, I, step * solver.dt, f"{output_dir}/step_{step:04d}.png")

    history_file.close()
    print(f"\n✅ Simulation Complete. Outputs in {output_dir}")


if __name__ == "__main__":
    run_simulation()
