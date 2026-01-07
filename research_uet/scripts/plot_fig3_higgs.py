import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(-1.5, 1.5, 200)
# Standard Model Higgs Potential
V_sm = 0.5 * (phi**2 - 1) ** 2

# UET Modified Potential (Recoil adds steepness at edges)
# Recoil ~ phi^4 * correction
V_uet = 0.5 * (phi**2 - 1) ** 2 + 0.1 * phi**4

plt.figure(figsize=(8, 6))
try:
    plt.style.use("seaborn-whitegrid")
except:
    pass

plt.plot(phi, V_sm, "k--", label="Standard Model Potential", linewidth=2)
plt.plot(phi, V_uet, "b-", label="UET Potential (with Recoil)", linewidth=3)
plt.axhline(0, color="gray", linewidth=0.5)

plt.xlabel(r"Field strength $\phi$", fontsize=12)
plt.ylabel(r"Potential $V(\phi)$", fontsize=12)
plt.title("Higgs Potential: Vacuum Stability", fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig("research_uet/Figures/Fig3_Higgs_Potential.png", dpi=300)
print("Plot Generated: research_uet/Figures/Fig3_Higgs_Potential.png")
