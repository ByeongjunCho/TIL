import math

def my_sqrt(n):
    a = 1
    b = n
    result = 0
    # while not math.isclose(result**2, n):
    while not abs(result**2-n) < 1e-10:
        result = (a+b) / 2
        if result**2 > n:
            b = result
        else:
            a = result
        # print(a**2)
    return result

print(my_sqrt(16))