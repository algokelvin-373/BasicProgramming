import matplotlib.pyplot as plt
from cn.utils.function_math import animate_plot

min_x, max_x = -10, 10
min_y, max_y = -10, 10

func = [
    lambda x: -x,
    lambda x: -2*x,
    lambda x: -3*x,
]

labels = [
    r'$y = -x$',
    r'$y = -2x$',
    r'$y = -3x$',
]

d_colors = ['red', 'blue', 'green']

# Animation Create Plot!
fig, ani = animate_plot(
    functions=func,
    fx=labels,
    colors=d_colors,
    x_min=min_x,
    x_max=max_x,
    y_min=min_y,
    y_max=max_y,
    labels=labels,
)

plt.show()