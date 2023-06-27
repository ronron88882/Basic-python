import math

def sekibun(f, a=0, b=1, n=100):
    h = (b - a) / n  # 区間幅
    result = (f(a) + f(b)) / 2  # 最初と最後の項の合計

    for i in range(1, n):
        x = a + i * h
        result += f(x)

    result *= h  # 積分値の計算

    return result

#(1)
def f(x):
    return math.sin(x)

a = 0
b = math.pi / 2
n = 50

answer = sekibun(f, a, b, n)
print("積分値:", answer)

#(2)
def f(x):
    return 4/(1+x**2)

a = 0
b = 1
n = 100

answer = sekibun(f, a, b, n)
print("積分値:", answer)

#(3)
def f(x):
    return math.sqrt(math.pi) * math.exp(-x**2)

a = -100
b = 100
n = 1000

answer = sekibun(f, a, b, n)
print("積分値:", answer)
