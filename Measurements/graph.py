import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# THREE EXPERIMENT DENSITY BAR GRAPHS
# ============================================================
# Experiment 1: 100 mL Graduated Cylinder
# Experiment 2: 50 mL Beaker
# Experiment 3: Penny
# ============================================================


# ============================================================
# EXPERIMENT 1
# 100 mL Graduated Cylinder
# ============================================================

initial_mass_1 = 44.80  # g

total_masses_1 = np.array([
    54.05,
    64.03,
    74.58,
    84.22,
    94.35
])

volume_per_trial_1 = 10  # mL

# Calculate mass added during each trial
masses_1 = np.diff(
    np.insert(total_masses_1, 0, initial_mass_1)
)

# Calculate density
densities_1 = masses_1 / volume_per_trial_1

trials_1 = np.arange(1, 6)

# Average density
average_density_1 = np.mean(densities_1)

# Calculate true density using cumulative mass vs. volume
volumes_1 = trials_1 * volume_per_trial_1
cumulative_mass_1 = total_masses_1 - initial_mass_1

slope_1, intercept_1 = np.polyfit(
    volumes_1,
    cumulative_mass_1,
    1
)

true_density_1 = slope_1


# ============================================================
# EXPERIMENT 2
# 50 mL Beaker
# ============================================================

initial_mass_2 = 33.80  # g

total_masses_2 = np.array([
    44.34,
    51.77,
    60.61,
    69.68
])

volume_per_trial_2 = 10  # mL

# Calculate mass added during each trial
masses_2 = np.diff(
    np.insert(total_masses_2, 0, initial_mass_2)
)

# Calculate density
densities_2 = masses_2 / volume_per_trial_2

trials_2 = np.arange(1, 5)

# Average density
average_density_2 = np.mean(densities_2)

# Calculate true density using cumulative mass vs. volume
volumes_2 = trials_2 * volume_per_trial_2
cumulative_mass_2 = total_masses_2 - initial_mass_2

slope_2, intercept_2 = np.polyfit(
    volumes_2,
    cumulative_mass_2,
    1
)

true_density_2 = slope_2


# ============================================================
# EXPERIMENT 3
# Penny
# ============================================================

# Penny measurements
penny_masses = np.array([
    2.51,
    2.51
])

diameter = 1.8  # cm
height = 0.11  # cm

# Calculate radius
radius = diameter / 2

# Calculate penny volume
penny_volume = np.pi * radius**2 * height

# Calculate density for each trial
densities_3 = penny_masses / penny_volume

trials_3 = np.arange(1, 3)

# Average density
average_density_3 = np.mean(densities_3)

# Since the penny has the same mass and volume for both trials,
# the measured density is also the true/calculated density.
true_density_3 = average_density_3


# ============================================================
# PRINT ALL RESULTS
# ============================================================

print("\n")
print("=" * 60)
print("EXPERIMENT 1 - 100 mL GRADUATED CYLINDER")
print("=" * 60)

for i in range(len(trials_1)):
    print(
        f"Trial {i + 1}: "
        f"Mass = {masses_1[i]:.2f} g | "
        f"Density = {densities_1[i]:.3f} g/mL"
    )

print(f"\nAverage Density: {average_density_1:.3f} g/mL")
print(f"True Density:    {true_density_1:.3f} g/mL")


print("\n")
print("=" * 60)
print("EXPERIMENT 2 - 50 mL BEAKER")
print("=" * 60)

for i in range(len(trials_2)):
    print(
        f"Trial {i + 1}: "
        f"Mass = {masses_2[i]:.2f} g | "
        f"Density = {densities_2[i]:.3f} g/mL"
    )

print(f"\nAverage Density: {average_density_2:.3f} g/mL")
print(f"True Density:    {true_density_2:.3f} g/mL")


print("\n")
print("=" * 60)
print("EXPERIMENT 3 - PENNY")
print("=" * 60)

print(f"Diameter: {diameter:.2f} cm")
print(f"Height:   {height:.2f} cm")
print(f"Radius:   {radius:.2f} cm")
print(f"Volume:   {penny_volume:.3f} cm³")

for i in range(len(trials_3)):
    print(
        f"Trial {i + 1}: "
        f"Mass = {penny_masses[i]:.2f} g | "
        f"Density = {densities_3[i]:.3f} g/mL"
    )

print(f"\nAverage Density: {average_density_3:.3f} g/mL")
print(f"True Density:    {true_density_3:.3f} g/mL")


# ============================================================
# GRAPHING FUNCTION
# ============================================================

def create_bar_graph(
    trials,
    densities,
    average_density,
    true_density,
    title,
    color,
    filename
):
    plt.figure(figsize=(10, 6))

    # Create bars
    bars = plt.bar(
        trials,
        densities,
        color=color,
        edgecolor="black",
        width=0.6
    )

    # Put density value above each bar
    for bar, density in zip(bars, densities):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + (max(densities) * 0.02),
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

    # Graph title
    plt.title(
        title,
        fontsize=15,
        fontweight="bold"
    )

    # Axis labels
    plt.xlabel(
        "Amount of Trials",
        fontsize=12
    )

    plt.ylabel(
        "Density (g/mL)",
        fontsize=12
    )

    # Trial labels
    plt.xticks(
        trials,
        [f"Trial {i}" for i in trials]
    )

    # Grid
    plt.grid(
        axis="y",
        linestyle=":",
        alpha=0.6
    )

    # Legend
    plt.legend()

    plt.tight_layout()

    # Save graph
    plt.savefig(
        filename,
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ============================================================
# CREATE EXPERIMENT 1 GRAPH
# ============================================================

create_bar_graph(
    trials_1,
    densities_1,
    average_density_1,
    true_density_1,
    "Experiment 1: Density Using a 100 mL Graduated Cylinder",
    "skyblue",
    "experiment_1_density.png"
)


# ============================================================
# CREATE EXPERIMENT 2 GRAPH
# ============================================================

create_bar_graph(
    trials_2,
    densities_2,
    average_density_2,
    true_density_2,
    "Experiment 2: Density Using a 50 mL Beaker",
    "orange",
    "experiment_2_density.png"
)


# ============================================================
# CREATE EXPERIMENT 3 GRAPH
# ============================================================

create_bar_graph(
    trials_3,
    densities_3,
    average_density_3,
    true_density_3,
    "Experiment 3: Density of a Penny",
    "gold",
    "experiment_3_density.png"
)


print("\n")
print("=" * 60)
print("ALL THREE GRAPHS HAVE BEEN CREATED!")
print("=" * 60)