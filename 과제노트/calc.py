def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'
        