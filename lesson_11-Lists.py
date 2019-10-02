# Primitive data types

some_num = 4
some_decimal = 3.14
some_str = 'Hello, SmartNinja!'
human = True

print('Primitiv data types')
print(type(some_num))
print(type(some_decimal))
print(type(some_str))
print(type(human))


print('')
print('')
print('')

# List
print('List')

some_list = [1, 34, 12, 17, 87]
print(some_list)
print(type(some_list))

print('')

another_list = ['tesla', 'toyota', 'nissan']
print(another_list)
print(type(another_list))

print('')

mixed_list = [22, 'elon', True, 'SmartNinja', 3.14]
print(mixed_list)
print(type(mixed_list))

print('')
print('')

# List Sorting
print('List - Sorting')

print('')

print(some_list)
some_list.sort()
print(some_list)

print('')
print('')

# List For-In loop
print('List - for-in loop')

print(another_list)

for item in another_list:
    print(item)
