import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the main plot
fig, ax = plt.subplots()
ax.plot(x, y, label='Main Plot')

# Create the inset plot
ax_inset = ax.inset_axes([0.6, 0.6, 0.35, 0.35])  # Specify the inset's position and size
ax_inset.plot(x, y, label='Inset Plot')

# Set properties of the inset plot
ax_inset.set_title('Inset Plot')
ax_inset.set_xticks([])
ax_inset.set_yticks([])

# Add legends
ax.legend()
ax_inset.legend()

# Show the plot
plt.show()
