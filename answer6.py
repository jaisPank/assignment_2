def arguments(*args, **kwargs):
    total = 0

    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg

    for value in kwargs.values():
        if isinstance(value, (int, float)):
            total += value

    return total


print(arguments(1, 2, 3, 4, 5, 6))
print(arguments(1, num1=4, num2=5))
print(arguments(num1=5, num2=2, num3=3))
