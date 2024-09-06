import numpy as np
import matplotlib.pyplot as plt

# Enable LaTeX-style text rendering
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Generate synthetic measured data
x_measured = np.array([ 0.  ,  1.11,  2.22,  3.33,  4.44,  5.56,  6.67,  7.78,  8.89,
       10.  ])
y_measured = np.array([0.29,  2.85,  5.55,  7.54,  9.08, 12.23, 13.94, 17.27,  18.50,  20.58])
# Define the error in measurement
y_error = np.array([0.51, 1.37, 1.14, 1.43, 1.34, 0.95, 1.38, 1.12, 0.7 , 0.7 ]) # Random errors for each point

# Plot the expected linear dependency (without noise)
x_line = np.linspace(0, 15, 100)  # More points to make the line smooth
y_line = 2 * x_line + 0.1

# Create a plot
plt.figure(figsize=(8, 6))
plt.plot(x_line, y_line, label=r'Ausgleichsgerade', color='red')
# Plot the measured data with error bars
plt.errorbar(x_measured, y_measured, yerr=y_error, fmt='o', label=r'Messdaten', capsize=5, color='k')

# LaTeX-formatted labels, title, and legend
plt.xlabel(r'$t$ (s)', fontsize=14)
plt.ylabel(r'$s$ (m)', fontsize=14)
plt.title(r'Title', fontsize=16)
plt.legend()

#
plt.xlim(0, 11)
plt.ylim(0, 22)

# Add a grid for better readability
plt.grid(True)

# Save the plot as a vector graphic (PDF format)
plt.savefig('plot.pdf', format='pdf')

# Show the plot
plt.show()
