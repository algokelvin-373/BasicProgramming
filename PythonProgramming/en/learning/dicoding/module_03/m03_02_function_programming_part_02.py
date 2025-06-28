print("***** Function: Pass by reference *****")


def _get_list_01(list_data):
    list_data.append([1, 2, 3, 4])
    print("The value of list in inside function = ", my_list)


def _get_list_02(list_data):
    list_data = [1, 2, 3, 4]
    print("The value of list in inside function = ", list_data)


my_list = [10, 20, 30]
_get_list_01(my_list)
print("The value of list in outside function = ", my_list)

print("***** Function: Pass by value *****")

my_list_02 = [10, 20, 30]
_get_list_02(my_list_02)
print("The value of list in outside function = ", my_list_02)
