import math


# def a(x):
#     return x**2
# lambda
def pangkat(x): return x**2


# def b(x, y):
#     return math.sqrt(x**2 + y**2)
# lambda
def double(x, y): return math.sqrt(x**2 + y**2)


def c(*args):
    return sum(args)/len(args)


# sum = lambda c(*args): sum(args)/len(args)


def d(s):
    return "".join(set(s))


my_list = [1, 3, 4, 5, 6, 7, 8, 9, 50, 8, 6, 22, 45, 66]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)


print(pangkat(10))
print(double(5, 10))
print(c(7, 8, 8, 9, 11))
