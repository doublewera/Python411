# Структура игры

from pole_q import questions

# 1. Создается загаданное слово, число и т.д. - 
# последовательность символов


# question = # Выбрать вопрос из словаря вопросов
# Найдите в кодах, презентациях и прошлых уроках способ, как выбрать
# случайным образом вопрос и ответ

word       = 'Академия'
zvezdochki = '********'

# Для любого языка!
zvezdochki = ''
for i in range(len(word)):
    zvezdochki += '*'

zvezdochki = '*' * len(word)  # Python!

zvezdochki = list(zvezdochki)  # чтобы можно было заменять на буквы!

# 2. Показать человеку вопрос и звездочки

# 3. 

print('Учебное заведение, в котором вы учитесь')

for i in word:  # по количеству букв в слове
    # Точно ли такое условие цикла?
    print(''.join(zvezdochki))  # join - это split наоборот - склеить строку
    user_answer = input('Введите букву или слово целиком: ')
    # Пользователь что-то ввел....
    # word       = 'Академия'
    # zvezdochki = '********'
    if user_answer in word:  # допустим, 'а'
        print('Есть такая буква в этом слове!')
        'Академия'
        'а*а*****'
        # вписано вручную! Не зависит от введенной буквы! ИССПРАВИТЬ!
        # И ПОЗИЦИЮ - ТОЖЕ!
        zvezdochki[0] = 'а'
        zvezdochki[2] = 'a'

    # Цикл в цикле?

# Можно усложнить игру, добавив ограничение по количеству попыток

