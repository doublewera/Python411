# Исключение - работа с нештатной ситуацией
# 1/0
result = 0
znam = int(input('Введите число, я найду обратное:'))
try:
    result = 1 / znam
except ZeroDivisionError:
    print('Я же говорю: не хочу делить на ноль!')
    result = None
print(result)