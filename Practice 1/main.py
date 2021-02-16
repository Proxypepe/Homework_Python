import math

def f11(x, y, z):
    return 81 * (y ** 4 / 51 - y ** 6) ** 8 - z - (42 * (70 * y + \
    x ** 2) ** 6 - abs(x) ) + math.sqrt(math.sin(x ** 6) + abs(x))

def f12(x):
    result = 0.0
    if x < 74:
        result = 83 * x ** 8 - 8 * x ** 6
    elif 73 <= x < 97:
        result = 92 * x ** 2 - math.tan(x)
    elif 97 <= x < 128:
        result = 53 * ( math.cos(x + math.exp(x) - 1) ** 7 + x ** 6)
    elif x >= 128:
        result = (x ** 3 / 15 + x ** 6) ** 6 - x ** 2
    return result

def f13(n, m):
    result = 0.0
    sub_sum = 0.0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            result += 81 * j ** 2 - abs(j)
    for i in range(1, n + 1):
         sub_sum += 34 * i ** 3 - math.sin(i)
    return 2 * result - sub_sum

def f14(n):
    if n == 0:
        return 4
    else:
        return 1/64 * f14(n - 1) - abs(f14(n - 1))
