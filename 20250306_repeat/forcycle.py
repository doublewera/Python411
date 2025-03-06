# Получите множество чисел, не делящихся на 6 от 1 до 100.
imax = 100
result = set()  # {} - empty DICT!
# print(14 % 5)  # % 5 :  {0, 1, 2, 3, 4}
for a in range(1, imax):
    if a % 6 != 0:   # Значит, НЕ ДЕЛИТСЯ, значит - ПОДХОДИТ!
        result = result | {a}
        result |= {a}   # одним движением и присвоили и объединили
print(result)