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

def animate_plot(f, fx, x_min, x_max, y_min, y_max, color='red'):
    figure, ax = plt.subplots(figsize=(8, 8))
    setup_axes(ax, x_min, x_max, y_min, y_max)
    ax.set_title(fx)

    # Calculate data
    x = np.linspace(x_min, x_max, 400)
    y = f(x)

    # Create line
    line, = ax.plot([], [], color=color, linewidth=2, label=fx)
    ax.legend()

    # Function init
    def init():
        line.set_data([], [])
        return line,

    # Function animation
    def animate(i):
        line.set_data(x[:i], y[:i])
        return line,

    # Create Animation!
    anim = animation.FuncAnimation(
        figure, animate, init_func=init,
        frames=len(x),
        interval=20,
        blit=True,
        repeat=True
    )
    return figure, anim

min_x, max_x = -5, 5
min_y, max_y = -5, 25
label =  r'$y = x^2$'

# Animation Create Plot!
fig, ani = animate_plot(
    f=lambda x: x**2,
    fx=label,
    x_min=min_x,
    x_max=max_x,
    y_min=min_y,
    y_max=max_y,
)

plt.show()