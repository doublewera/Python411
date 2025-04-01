печать = print  # ВАЖНО! БЕЗ СКОБОК!
печать("Я умею печатать")
if callable(печать):
    # callable проверяет, является ли её аргумент функцией
    print('Это функция! печать')
else:
    print('Это не функция печать')

chislo = 25
if callable(chislo):
    # callable проверяет, является ли её аргумент функцией
    print('Это функция!', chislo)
else:
    print('Это не функция', chislo)
help(callable)
help(24 )