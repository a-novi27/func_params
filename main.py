def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

list_ = [1, 2, 3]
print_params(*list_)
print_params(b = 25)
print_params(c = [1,2,3])


values_list = (True, 12, 'false')
values_dikt = {'a': 2, 'b': 6, 'c': 9}

print_params(*values_list)
print_params(**values_dikt)

values_list_2 = ('z', 17)
print_params(*values_list_2, 42)
