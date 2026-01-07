"""
UET Matrix Engine - Tensor-Based Reality Simulation (v0.9 Core)
================================================================

This module implements the "Matrix Form" of UET.
Instead of calculating specific functions (f(x)), we evolve a State Tensor (S).

Key Concepts:
-------------
1. State Tensor (S): A 4D tensor representing [Energy, Information, Space, Time] at every point.
2. Evolution Operator (T): A Transformation Matrix that evolves S_t -> S_t+1.
3. Coordinate Invariance: Operations are Tensor Contractions, valid in any frame.

Mathematical Form:
------------------
S_{t+1} = T • S_t

where:
- S is the Universe State
- T is the Transfer Tensor (Encoding Physical Laws like Gravity & Entropy)
"""

import numpy as np
from dataclasses import dataclass


@dataclass
class UniverseState:
    """
    Represents the state of a system as a Tensor.

    Layers (Rank-1 Indices):
    0: Mass/Energy Density (ρ) - Gravity Source
    1: Information Density (σ) - Structure Source
    2: Energy Flux X (Vx) - Flow
    3: Energy Flux Y (Vy) - Flow
    4: Energy Flux Z (Vz) - Flow
    """

    grid_size: int
    tensor: np.ndarray  # Shape: (5, N, N, N) for 3D grid

    def __init__(self, size: int):
        self.grid_size = size
        # Initialize empty 5-layer tensor (Mass, Info, Vx, Vy, Vz)
        self.tensor = np.zeros((5, size, size, size))

    @property
    def density(self):
        return self.tensor[0]

    @property
    def information(self):
        return self.tensor[1]


class MatrixEvolution:
    """
    The Physics Engine that evolves the Universe State via Matrix Operations.
    """

    def __init__(self, G: float = 1.0, c: float = 1.0, beta: float = 0.5):
        self.G = G
        self.c = c
        self.beta = beta  # Information Coupling

    def _get_laplacian_kernel(self) -> np.ndarray:
        """Standard 3x3x3 Laplacian Kernel for 3D Grid."""
        # 3D Laplacian: center -6, neighbors +1
        k = np.zeros((3, 3, 3))

        # Center
        k[1, 1, 1] = -6.0

        # Neighbors (Face-connected)
        k[0, 1, 1] = 1.0
        k[2, 1, 1] = 1.0
        k[1, 0, 1] = 1.0
        k[1, 2, 1] = 1.0
        k[1, 1, 0] = 1.0
        k[1, 1, 2] = 1.0

        return k

    def _apply_convolution(self, field: np.ndarray, kernel: np.ndarray) -> np.ndarray:
        """
        Applies a 3D spatial convolution.
        In a full tensor form, this is T_xyzw * S_xy.
        Using scipy.signal.convolve2d (or manual) for PoC speed.
        """
        # Manual naive convolution for transparency/numpy-only
        size = field.shape[0]
        k_size = kernel.shape[0]
        pad = k_size // 2

        # Pad field
        padded = np.pad(field, pad, mode="edge")
        output = np.zeros_like(field)

        # This loop is slow in Python, but conceptually correct for "Matrix Op" representation
        # optimized version would use FFT
        for i in range(size):
            for j in range(size):
                for k in range(size):  # Added Z-loop
                    region = padded[i : i + k_size, j : j + k_size, k : k + k_size]
                    output[i, j, k] = np.sum(region * kernel)

        return output

    def _get_gradient_kernels(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Simple Central Difference Gradient Kernels (3D)."""
        # 3D Kernels (3x3x3)
        kx = np.zeros((3, 3, 3))
        ky = np.zeros((3, 3, 3))
        kz = np.zeros((3, 3, 3))  # Added Z-gradient

        # d/dx (along axis 0)
        kx[0, 1, 1] = -0.5
        kx[2, 1, 1] = 0.5

        # d/dy (along axis 1)
        ky[1, 0, 1] = -0.5
        ky[1, 2, 1] = 0.5

        # d/dz (along axis 2)
        kz[1, 1, 0] = -0.5
        kz[1, 1, 2] = 0.5

        return kx, ky, kz

    def _advect(
        self, field: np.ndarray, vx: np.ndarray, vy: np.ndarray, vz: np.ndarray
    ) -> np.ndarray:
        """
        Computes 3D Advection: (v . del) field = vx * dF/dx + vy * dF/dy + vz * dF/dz
        """
        kx, ky, kz = self._get_gradient_kernels()
        grad_x = self._apply_convolution(field, kx)
        grad_y = self._apply_convolution(field, ky)
        grad_z = self._apply_convolution(field, kz)
        return vx * grad_x + vy * grad_y + vz * grad_z

    def compute_interaction_matrix(self, S: UniverseState) -> np.ndarray:
        """
        Generates the Interaction Matrix using Kernels.
        """
        N = S.grid_size
        rho = S.density
        sigma = S.information

        # 1. Metric Strain (Space deformation)
        laplacian_kernel = self._get_laplacian_kernel()
        metric_strain = self._apply_convolution(rho, laplacian_kernel)

        # 2. Information Pressure
        info_pressure = self.beta * sigma

        # Total Interaction
        interaction_linear = metric_strain + info_pressure

        # 3. Nonlinear Saturation (Sigmoid/Tanh)
        interaction_saturated = np.tanh(interaction_linear / 1000.0) * 1000.0

        return interaction_saturated

    def step(self, S: UniverseState, dt: float = 0.1) -> UniverseState:
        """
        Evolve state: S_new = S_old + dt * (Interactions)
        """
        S_new = UniverseState(S.grid_size)

        # Extract Layers
        rho = S.tensor[0]
        sigma = S.tensor[1]
        vx = S.tensor[2]  # Flux X (Fluid Velocity)
        vy = S.tensor[3]  # Flux Y (Fluid Velocity)
        vz = S.tensor[4]  # New Z-velocity

        # --- 1. Forces & Potentials ---
        interaction = self.compute_interaction_matrix(S)
        laplacian_kernel = self._get_laplacian_kernel()

        # --- 2. Flux Evolution (Navier-Stokes Momentum) ---
        # dv/dt = - (v.grad)v + viscosity * del^2 v
        viscosity = 0.01

        # Advection of Momentum
        advect_vx = self._advect(vx, vx, vy, vz)
        advect_vy = self._advect(vy, vx, vy, vz)
        advect_vz = self._advect(vz, vx, vy, vz)

        # Diffusion of Momentum (Viscosity)
        diff_vx = self._apply_convolution(vx, laplacian_kernel)
        diff_vy = self._apply_convolution(vy, laplacian_kernel)
        diff_vz = self._apply_convolution(vz, laplacian_kernel)

        # Update Velocity
        S_new.tensor[2] = vx + dt * (-advect_vx + viscosity * diff_vx)
        S_new.tensor[3] = vy + dt * (-advect_vy + viscosity * diff_vy)
        S_new.tensor[4] = vz + dt * (-advect_vz + viscosity * diff_vz)

        # --- 3. Mass Evolution (Continuity Equation) ---
        # dRho/dt = - div(Rho * v) + Sources
        # Simplified: dRho/dt = - (v.grad)Rho + Diffusion + Interaction

        # Mass Advection
        advect_rho = self._advect(rho, vx, vy, vz)

        # Mass Diffusion & Interaction
        diff_rho = self._apply_convolution(rho, laplacian_kernel)

        # Update Density
        # Note: We add `interaction` as a "Source/Sink" term (Gravity/Formation)
        S_new.tensor[0] = rho + dt * (-advect_rho + 0.01 * diff_rho + 0.01 * interaction)

        # --- 4. Information Evolution ---
        # Info grows where there is energy density
        S_new.tensor[1] = sigma + dt * (rho * self.beta)

        return S_new


def create_galaxy_initial_state(size: int = 50) -> UniverseState:
    """Creates a 'Galaxy' state vector (High density in center)."""
    state = UniverseState(size)
    center = size // 2

    # Create Gaussian distribution
    for i in range(size):
        for j in range(size):
            r2 = (i - center) ** 2 + (j - center) ** 2
            state.tensor[0, i, j] = 100 * np.exp(-r2 / 20.0)  # Mass

    return state
