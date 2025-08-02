# function general
def get_begin():
    return 'Python编程'

# function with parameter
def get_name(name):
    return f'我是{name}'

print(get_begin())
data = input('输入您的姓名：')
print(get_name(data))