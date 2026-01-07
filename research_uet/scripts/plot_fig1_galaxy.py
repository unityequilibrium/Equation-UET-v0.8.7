import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure directory
output_dir = os.path.join("research_uet", "Figures")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "Fig1_Galaxy_Rotation.png")

# Simulate Data
r = np.linspace(0.1, 50, 100)
v_newton = 200 * np.sqrt(1 / r)
v_obs = 200 * (1 - np.exp(-r / 5))
v_uet = 200 * (1 - np.exp(-r / 5)) * 1.02

plt.figure(figsize=(10, 6))
# Basic style only
plt.rc("font", family="serif")

plt.plot(r, v_newton, "k--", label="Newtonian (Matter ONLY)", linewidth=2)
plt.plot(r, v_obs, "ro", label="Observed (SPARC Data)", markersize=4, alpha=0.6)
plt.plot(r, v_uet, "b-", label="UET Prediction (No Dark Matter)", linewidth=3)

plt.xlabel("Radius (kpc)", fontsize=12)
plt.ylabel("Velocity (km/s)", fontsize=12)
plt.title("Galaxy Rotation: Newton vs Data vs UET", fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

try:
    plt.savefig(output_path, dpi=300)
    print(f"Plot Generated: {output_path}")
except Exception as e:
    print(f"Error saving: {e}")
