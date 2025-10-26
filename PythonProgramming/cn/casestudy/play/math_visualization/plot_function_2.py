import matplotlib.pyplot as plt
import numpy as np

def create_plot(f, fx, x_min, x_max, y_min, y_max):
    # Setting range
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    # Draw line X and Y
    ax.axhline(0, color='black', linewidth=0.8)  # X (horizontal)
    ax.axvline(0, color='black', linewidth=0.8)  # Y (vertical)

    # Add grid
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Setting ticks
    ax.set_xticks(range(x_min, x_max + 1))
    ax.set_yticks(range(y_min, y_max + 1))

    # Add label
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    x = np.linspace(x_min, x_max, 400)
    y = f(x)
    ax.plot(x, y, color='red', label=fx)
    ax.legend()

min_x = -10
max_x = 10
min_y = -10
max_y = 10

label = 'y = x'
fig, ax = plt.subplots(figsize=(8, 8))  # Make figure dan axis

# Create Plot
create_plot(
    lambda x: x,
    label,
    min_x,
    max_x,
    min_y,
    max_y
)

plt.title(label)                        # Title Graphic
plt.show()                              # Show