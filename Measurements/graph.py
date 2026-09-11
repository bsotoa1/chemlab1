#This code produces bar graph for the measurements lab

import numpy as np
import matplotlib.pyplot as plt

# Initial mass of empty graduated cylinder
initial_mass = 44.80  # g

# Total masses after each 10 mL addition
total_masses = np.array([
    54.05,
    64.03,
    74.58,
    84.22,
    94.35
])

# Calculate mass added for each trial
masses = np.diff(np.insert(total_masses, 0, initial_mass))

# Volume for each trial
volume = 10  # mL

# Calculate density
densities = masses / volume

# Trial numbers
trials = np.arange(1, 6)

# Average density
average_density = np.mean(densities)

# True density from mass vs. volume best-fit line
volumes = trials * volume
cumulative_mass = total_masses - initial_mass

slope, intercept = np.polyfit(volumes, cumulative_mass, 1)
true_density = slope

# Print results
print("Density Measurements at 20 °C")
print("--------------------------------")

for i in range(5):
    print(
        f"Trial {i+1}: "
        f"Mass = {masses[i]:.2f} g, "
        f"Density = {densities[i]:.3f} g/mL"
    )

print("--------------------------------")
print(f"Average Density = {average_density:.3f} g/mL")
print(f"True Density = {true_density:.3f} g/mL")

# =========================
# BAR GRAPH
# =========================

plt.figure(figsize=(10, 6))

bars = plt.bar(
    trials,
    densities,
    color="skyblue",
    edgecolor="black",
    width=0.6
)

# Add density values above each bar
for bar, density in zip(bars, densities):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.005,
        f"{density:.3f}",
        ha="center",
        fontsize=10,
        fontweight="bold"
    )

# Average density line
plt.axhline(
    average_density,
    color="green",
    linestyle="--",
    linewidth=2,
    label=f"Average Density = {average_density:.3f} g/mL"
)

# True density line
plt.axhline(
    true_density,
    color="red",
    linestyle="-",
    linewidth=2,
    label=f"True Density = {true_density:.3f} g/mL"
)

# Labels and title
plt.title(
    "Density Measured at 20 °C\n"
    "100 mL Graduated Cylinder",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Trials", fontsize=12)
plt.ylabel("Density (g/mL)", fontsize=12)

plt.xticks(
    trials,
    ["Trial 1", "Trial 2", "Trial 3", "Trial 4", "Trial 5"]
)

# Start y-axis near zero so bars are represented correctly
plt.ylim(0, 1.15)

plt.grid(axis="y", linestyle=":", alpha=0.6)

plt.legend()
plt.tight_layout()

plt.show()
