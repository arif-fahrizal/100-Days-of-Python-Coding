def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]

    return n

# print(add(9,9,9,8,7,6,5,4,3))
print(calculate(2, add=90, multiply=2))