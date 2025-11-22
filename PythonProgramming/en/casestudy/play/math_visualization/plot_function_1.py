import matplotlib.pyplot as plt

def create_plot(x_min, x_max, y_min, y_max):
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


min_x = -10
max_x = 10
min_y = -10
max_y = 10

fig, ax = plt.subplots(figsize=(8, 8))  # Make figure dan axis
create_plot(min_x, max_x, min_y, max_y) # Create Plot
plt.title('X and Y')                    # Title Graphic
plt.show()                              # Show