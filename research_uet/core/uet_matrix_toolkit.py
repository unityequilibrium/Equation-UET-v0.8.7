"""
UET Matrix Toolkit (v0.9 Beta)
==============================
Utilities for configuring and verifying Matrix Simulations.
- MatrixConfig: Loads parameters from JSON.
- MatrixVisualizer: Generates Heatmaps/Plots from UniverseState tensors.
"""

import json
import os
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class MatrixConfig:
    grid_size: int
    dt: float
    beta: float
    steps: int
    output_dir: str

    @classmethod
    def from_json(cls, filepath: str) -> "MatrixConfig":
        with open(filepath, "r") as f:
            data = json.load(f)

        return cls(
            grid_size=data.get("grid_size", 50),
            dt=data.get("dt", 0.1),
            beta=data.get("beta", 0.5),
            steps=data.get("steps", 100),
            output_dir=data.get("output_dir", "outputs/matrix_runs"),
        )


class MatrixVisualizer:
    @staticmethod
    def plot_heatmap(tensor_slice: np.ndarray, title: str, filename: str):
        """
        Generates a heatmap image from a 2D matrix slice.
        """
        plt.figure(figsize=(10, 8))
        plt.imshow(tensor_slice, cmap="viridis", origin="lower")
        plt.colorbar(label="Density / Intensity")
        plt.title(title)

        # Ensure directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        plt.savefig(filename)
        plt.close()
        print(f"saved heatmap: {filename}")

    @staticmethod
    def plot_state_layers(state, output_prefix: str):
        """
        Plots Mass, Information, and Flux layers.
        """
        MatrixVisualizer.plot_heatmap(
            state.tensor[0], "Mass Density (Layer 0)", f"{output_prefix}_mass.png"
        )
        MatrixVisualizer.plot_heatmap(
            state.tensor[1], "Information Density (Layer 1)", f"{output_prefix}_info.png"
        )
        MatrixVisualizer.plot_heatmap(
            state.tensor[2], "Flux/Field (Layer 2)", f"{output_prefix}_flux.png"
        )
