# this functions does nothing!
def do_nothing():
    pass

# def print_banner():
#     print("=======================")
#     print("Insert banner text here")
#     print("=======================")

# Must call function AFTER its defined to execute it
# print_banner()


# text is a parameter
# Must give the parameter a value when calling the function
def print_banner(text):
    print("=======================")
    print(text)
    print("=======================")

print_banner('text here')


# def sum(*args):
#     print(type(args))
#     # prints: <class 'tuple'>

#     total = 0
#     for arg in args:
#         total += arg

#     return total

# print(sum(1, 5, 10))
# # prints: 16


def sum(greeting, *args):
    print(greeting)
    # prints: Hello, friend

    total = 0
    for arg in args:
        total += arg

    return total

print(sum("Hello, friend", 1, 5, 10))
# prints:
# Hello, friend
# 16

# Argument and Paramater must match when passing a KWARG 
def make_an_employee(role):
    print(role)
    # prints: CEO

    employee = {"role": role}
    return employee

print(make_an_employee(role="CEO"))
# prints: { 'role': 'CEO' }


# Keyword Args are NOT positional but must come AFTER positional args
def make_employee(role, **kwargs):
    print(kwargs)
    # prints: {'first': 'Sam', 'middle': 'Harris', 'last': 'Altman'}
    print(type(kwargs))
    # prints: <class 'dict'>
    # kwargs is a dictionary - you can use it anywhere you'd use one:
    employee = {"role": role, "name": kwargs}
    return employee

print(make_employee("CEO", first="Sam", middle="Harris", last="Altman"))
# prints: {
#     'role': 'CEO',
#     'name': {'first': 'Sam', 'middle': 'Harris', 'last': 'Altman'}
# }

print(make_employee(first="Sam", middle="Harris", last="Altman", role="CEO"))
# prints: {
#     'role': 'CEO',
#     'name': {'first': 'Sam', 'middle': 'Harris', 'last': 'Altman'}
# }



def arg_demo(pos1, pos2, *args, **kwargs):
    print(f'Positional params: {pos1}, {pos2}')
    print('*args:')
    for arg in args:
        print(' ', arg)
    print('**kwargs:')
    for keyword, value in kwargs.items():
        print(f'  {keyword}: {value}')

arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')
