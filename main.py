def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params()


def print_params1(a, b, c):
    print(a, b, c)
values_list = [1, 'string', True]
values_dict = {'a': 1, 'b': 'string', 'c' : True}


print_params1(*values_list)
print_params1(**values_dict)


def print_params(a, b):
    print(a, b)

values_list_2 = [54.32, 'Строка' ]
print_params(values_list_2, 42)
