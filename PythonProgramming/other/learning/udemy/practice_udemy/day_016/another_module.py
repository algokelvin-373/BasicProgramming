variable_in_module = 100

def times_moves(my_turtle, times):
    start = 1
    while start <= times:
        my_turtle.forward(100)
        my_turtle.backward(50)
        start += 1