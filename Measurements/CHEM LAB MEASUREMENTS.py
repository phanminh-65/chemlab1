#This code produces the bar graph for the measurements lab
import numpy as np
import matplotlib.pyplot as plt

# Density measurements (g/mL)
densities = np.array([1.017, 0.951, 0.956, 0.976, 0.974])

# Calculate average and sample standard deviation
average = np.mean(densities)
std_dev = np.std(densities, ddof=1)

# Measurement numbers
measurements = np.arange(1, 6)

# Create bar graph
plt.figure(figsize=(9, 6))

plt.bar(
    measurements,
    densities,
    yerr=std_dev,
    capsize=5,
    label="Density measurements ± SD"
)

# Average density line
plt.axhline(
    average,
    linestyle="--",
    linewidth=2,
    label=f"Average = {average:.3f} g/mL"
)

# True density line
plt.axhline(
    1.00,
    linestyle="-",
    linewidth=2,
    label="True density = 1.00 g/mL"
)

# Labels and title
plt.xlabel("Measurement")
plt.ylabel("Density (g/mL)")
plt.title("Density of Water at 25°C Obtained with the Graduated Cylinder")

# X-axis labels
plt.xticks(measurements)

# Set y-axis range
plt.ylim(0.85, 1.10)

# Add legend and grid
plt.legend()
plt.grid(axis="y", linestyle=":", alpha=0.5)

# Adjust spacing
plt.tight_layout()

# Display graph
plt.show()

# Print calculated values
print(f"Average density = {average:.3f} g/mL")
print(f"Sample standard deviation = {std_dev:.3f} g/mL")