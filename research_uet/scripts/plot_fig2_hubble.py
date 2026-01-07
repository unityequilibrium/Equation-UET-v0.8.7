import numpy as np
import matplotlib.pyplot as plt

# Data
# H0 values: [Value, Error]
planck = [67.4, 0.5]
shoes = [73.0, 1.0]
trgb = [69.8, 0.8]
uet_prediction = [69.9, 0.2]  # Derived from UET master equation

labels = ["Planck (CMB)", "TRGB (Stars)", "SH0ES (Supernova)", "UET (Information)"]
values = [planck[0], trgb[0], shoes[0], uet_prediction[0]]
errors = [planck[1], trgb[1], shoes[1], uet_prediction[1]]
colors = ["blue", "green", "red", "purple"]

plt.figure(figsize=(8, 6))
# Try to use a clean style
try:
    plt.style.use("seaborn-whitegrid")
except:
    pass

for i in range(len(values)):
    plt.errorbar(
        i,
        values[i],
        yerr=errors[i],
        fmt="o",
        color=colors[i],
        ecolor=colors[i],
        elinewidth=3,
        capsize=5,
        markersize=10,
    )
    plt.text(i + 0.1, values[i], f"{values[i]}", va="center", fontweight="bold", color=colors[i])

plt.xticks(range(len(labels)), labels, fontsize=11)
plt.ylabel("H0 (km/s/Mpc)", fontsize=12)
plt.title("Hubble Tension: UET as the Bridge", fontsize=14)
plt.grid(axis="y", alpha=0.3)
plt.axhline(
    y=uet_prediction[0], color="purple", linestyle="--", alpha=0.3, label="UET Theoretical Value"
)

# Add "Tension Zone"
plt.axhspan(planck[0] - planck[1], planck[0] + planck[1], color="blue", alpha=0.1)
plt.axhspan(shoes[0] - shoes[1], shoes[0] + shoes[1], color="red", alpha=0.1)

plt.savefig("research_uet/Figures/Fig2_Hubble_Tension.png", dpi=300)
print("Plot Generated: research_uet/Figures/Fig2_Hubble_Tension.png")
