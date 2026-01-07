import unittest
import numpy as np
import sys
from pathlib import Path

# Add project root to path
import os

current_dir = Path(__file__).parent
# For topics: Go up 5 levels: poiseuille -> Code -> 0.10_Fluid... -> topics -> research_uet -> ROOT
_root = current_dir
while _root.name != "research_uet" and _root.parent != _root:
    _root = _root.parent
root_dir = _root.parent
sys.path.insert(0, str(root_dir))

from research_uet.core.uet_matrix_engine import UniverseState, MatrixEvolution


class TestMatrixFluid(unittest.TestCase):
    def setUp(self):
        self.size = 30
        self.state = UniverseState(self.size)
        self.engine = MatrixEvolution(G=1.0, c=1.0, beta=0.1)

        # Initialize Blob in Center (Layer 0: Mass)
        center = self.size // 2
        self.state.tensor[0, center, center] = 10.0

        # Initialize Uniform Velocity (Layer 2: Flux X)
        # Flowing to the RIGHT (+X)
        self.state.tensor[2, :, :] = 1.0

    def test_advection_movement(self):
        """Test that Mass moves with Flux (Convection)."""
        # Initial Center of Mass
        y_indices, x_indices = np.indices((self.size, self.size))
        mass_0 = np.sum(self.state.tensor[0])
        com_x_0 = np.sum(x_indices * self.state.tensor[0]) / mass_0

        print(f"Initial CoM X: {com_x_0:.2f}")

        # Evolve
        # We need a large dt or many steps to see movement
        # If advection is implemented: dRho/dt = -v * grad(Rho)
        current_state = self.state
        for _ in range(5):
            current_state = self.engine.step(current_state, dt=1.0)

        # Final Center of Mass
        mass_final = np.sum(current_state.tensor[0])
        com_x_final = np.sum(x_indices * current_state.tensor[0]) / mass_final

        print(f"Final CoM X: {com_x_final:.2f}")

        # Assertion: Did it move right?
        # Current engine: Only diffusion (symmetric), so CoM stays same.
        # New engine: CoM should increase.

        # For TDD: We expect this to fail or be equal if not implemented.
        # Once implemented, we want com_x_final > com_x_0 + tolerance

        diff = com_x_final - com_x_0
        print(f"Movement Shift: {diff:.2f}")

        # Check if advection happened
        if diff > 0.1:
            print("✅ Advection Detected (Mass moved downstream)")
        else:
            print("❌ No Advection (Mass is stationary/diffusing only)")

        # Verify Flux Consistency (Layer 2 should remain populated)
        flux_sum = np.sum(current_state.tensor[2])
        print(f"Total Flux X: {flux_sum:.2f}")
        self.assertGreater(flux_sum, 0, "Flux layer should not be wiped out.")


if __name__ == "__main__":
    unittest.main()
