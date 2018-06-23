# # for Loops
# people = ['Vuk', 'Mark', 'Nick']
#
# for person in people:
#     print('Name: ', person)
#
# for i in range(10):
#     print(i)
#
# for i in range(0, 10):
#     print(i)
#
# for i in range(-5, 5):
#     print(i)
# # while loops
# i = 0
# while i < 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# functions


def say_hello(name='John'):
    print('Hello ', name)
    return


say_hello()
say_hello('Vuk')


def get_sum(num1, num2):
    return num1 + num2


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def add_one_to_list(l):
    l.append(4)
    return


def my_pow(n, i=2):
    if i == 0:
        return 1
    if i == 1:
        return n
    return n * my_pow(n, i - 1)


print('pow -> ', my_pow(10, 1))
print('normal pow -> ', my_pow(10))

my_list = [1, 2, 3]
print(my_list, add_one_to_list(my_list))
print(get_sum(1, 5))
print(fact(5))

my_str = 'vuk is Cool.'
print(my_str.capitalize())
print(my_str.swapcase())
print(my_str.lower())
print(my_str.replace('vuk', 'nick'))
print(my_str.count('o'))
print(my_str.startswith('vu'))
print(my_str.endswith('.'))
print(my_str.split(' '))  # == print(my_str.split())
print(my_str.index('v'))
