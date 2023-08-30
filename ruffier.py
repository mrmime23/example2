# Модуль для расчета результатов

# Здесь должен быть твой код
def Function_1(aA, bB, cC):
    eE = (4*(aA+bB+cC) - 200)/10
    return eE

def dATA(dD):
    Temp = (min(dD, 15) - 7 ) // 2
    F = 21 - Temp * 1.5
    return F

def Process(E, fF):
    if E >= fF:
        return 0
    fF -= 4
    if E >= fF:
        return 1
    fF -= 5
    if E >= fF:
        return 2
    fF -= 5.5
    if E >= fF:
        return 3
    return 4

def eXecute(a, B, C, d):
    Ee = Function_1(a, B, C)
    Rresult = Process(Ee, dATA(d))
    if Rresult == 0:
        return "Низкий"
    elif Rresult == 1:
        return "Удв"
    elif Rresult == 2:
        return "Средний"
    elif Rresult == 3:
        return "Выше среднего"
    elif Rresult == 4:
        return "Высокий"
