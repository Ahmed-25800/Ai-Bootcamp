import sys
import numpy as np
import matplotlib.pyplot as plt

# 1. Print verification messages to the console
print("-" * 50)
print("SUCCESS: Your Anaconda environment is successfully linked!")
print("Python Version:", sys.version)
print("NumPy Version Installed:", np.__version__)
print("-" * 50)

# 2. Generate data points using NumPy
# Creates 100 points between 0 and 2*pi
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# 3. Create a clean plot using Matplotlib
plt.figure(figsize=(8, 4))
plt.plot(x, y, label="Sine Wave", color="dodgerblue", linewidth=2)
plt.title("Anaconda & VS Code Verification Plot", fontsize=14, fontweight="bold")
plt.xlabel("Angle (radians)")
plt.ylabel("Amplitude")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# 4. Display the window
print("Opening the verification plot window... Close the window to finish.")
plt.show()
