def yc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def sosuu(a, b):
    so = yc(a, b)
    if so == 1:
        return True
    else:
        return False

#1
sosuu(10,20)
yc(10,20)

#2
sosuu(14,91)
yc(14,91)

#3
sosuu(91,14)
yc(91,14)
