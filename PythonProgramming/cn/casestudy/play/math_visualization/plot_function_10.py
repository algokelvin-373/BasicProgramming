import matplotlib.pyplot as plt

from cn.utils.function_math import animate_plot

min_x, max_x = -10, 10
min_y, max_y = -10, 10

func = [
    lambda x: x**2 + x - 2,
    lambda x: x**2 + x - 1,
    lambda x: x**2 + x,
    lambda x: x**2 + x + 1,
    lambda x: x**2 + x + 2,
]

labels = [
    r'$y = x^2 + x - 2$',
    r'$y = x^2 + x - 1$',
    r'$y = x^2 + x$',
    r'$y = x^2 + x + 1$',
    r'$y = x^2 + x + 2$',
]

d_colors = [
    'blue',
    'green',
    'red',
    'orange',
    'purple',
]

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