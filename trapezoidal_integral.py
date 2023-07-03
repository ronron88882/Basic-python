import math

def f(x):
    return math.sin(x)

def trapezoidal(a, b, n):
    h = (b - a) / n
    result = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        x = a + i * h
        result += f(x)
    result *= h
    return result

a = 0
b = 0.5 * math.pi
n = 100

y = trapezoidal(a, b, n)
print(y)
