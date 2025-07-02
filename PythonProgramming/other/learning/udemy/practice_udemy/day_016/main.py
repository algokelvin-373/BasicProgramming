import another_module
from turtle import Screen, Turtle

print('Print value variable in another_module:')
print(another_module.variable_in_module)

print('Make object to show Turtle')
my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle.color('coral')
another_module.times_moves(my_turtle, 5)

print('Print my screen from Turtle')
my_screen = Screen()
print(f'Width  : {my_screen.canvwidth}')
print(f'Height : {my_screen.canvheight}')
my_screen.exitonclick()