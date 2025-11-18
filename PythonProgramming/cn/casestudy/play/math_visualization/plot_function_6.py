import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def setup_axes(axis, x_min, x_max, y_min, y_max):
    axis.set_xlim(x_min, x_max)
    axis.set_ylim(y_min, y_max)
    axis.axhline(0, color='black', linewidth=0.8)
    axis.axvline(0, color='black', linewidth=0.8)
    axis.grid(True, which='both', linestyle='--', linewidth=0.5)
    axis.set_xticks(range(x_min, x_max + 1))
    axis.set_yticks(range(y_min, y_max + 1))
    axis.set_xlabel('X')
    axis.set_ylabel('Y')

def animate_plot(functions, fx, colors, x_min, x_max, y_min, y_max):
    figure, ax = plt.subplots(figsize=(8, 8))
    setup_axes(ax, x_min, x_max, y_min, y_max)
    ax.set_title(fx)

    # Calculate data
    x = np.linspace(x_min, x_max, 400)
    y_data = [f(x) for f in functions]

    # Create line
    lines = []
    for label, color in zip(labels, colors):
        line, = ax.plot([], [], color=color, linewidth=2, label=label)
        lines.append(line)
    ax.legend()

    # Function init
    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    # Function animation
    def animate(i):
        for line, y in zip(lines, y_data):
            line.set_data(x[:i], y[:i])
        return lines

    # Create Animation!
    anim = animation.FuncAnimation(
        figure, animate, init_func=init,
        frames=len(x),
        interval=20,
        blit=True,
        repeat=True
    )
    return figure, anim

min_x, max_x = -10, 10
min_y, max_y = -10, 10

func = [
    lambda x: x,
    lambda x: x - 1,
    lambda x: x - 2,
    lambda x: x - 3,
]

labels = [
    r'$y = x$',
    r'$y = x - 1$',
    r'$y = x - 2$',
    r'$y = x - 3$',
]

d_colors = ['red', 'green', 'blue', 'orange']

# Animation Create Plot!
fig, ani = animate_plot(
    functions=func,
    fx=labels,
    colors=d_colors,
    x_min=min_x,
    x_max=max_x,
    y_min=min_y,
    y_max=max_y,
)

plt.show()