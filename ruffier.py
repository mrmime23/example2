# Модуль для расчета результатов

# Здесь должен быть твой код
def function1(a, b, c):
    e = (4*(a+b+c) - 200)/10
    return e

def data(d):
    temp = (min(d, 15) - 7 ) // 2
    f = 21 - temp * 1.5
    return f

def process(e, f):
    if e >= f:
        return 0
    f -= 4
    if e >= f:
        return 1
    f -= 5
    if e >= f:
        return 2
    f -= 5.5
    if e >= f:
        return 3
    return 4

def execute(a, b, c, d):
    e = function1(a, b, c)
    result = process(e, data(d))
    if result == 0:
        return "Низкий"
    elif result == 1:
        return "Удв"
    elif result == 2:
        return "Средний"
    elif result == 3:
        return "Выше среднего"
    elif result == 4:
        return "Высокий"
