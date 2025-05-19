from functools import reduce


def doubless(n):
    return n*2

def add(x,y):
    return x+y

def is_even(n):
    return n%2==0

number = [1,2,3,4,5]
resulta = list(filter(is_even,number))
print(resulta)

