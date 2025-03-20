# Структура игры

import random
from pole_q import questions

# 1. Создается загаданное слово, число и т.д. - 
# последовательность символов


# question = # Выбрать вопрос из словаря вопросов
# Найдите в кодах, презентациях и прошлых уроках способ, как выбрать
# случайным образом вопрос и ответ

word       = 'Академия'
word = random.choice(list(questions.keys()))
zvezdochki = '********'

# Для любого языка!
zvezdochki = ''
for i in range(len(word)):
    zvezdochki += '*'

zvezdochki = '*' * len(word)  # Python!

zvezdochki = list(zvezdochki)  # чтобы можно было заменять на буквы!

# 2. Показать человеку вопрос и звездочки

# Как сделать все буквы маленькими?

print(word.lower())  # только печатает, НЕ МЕНЯЕТ СЛОВО!
print(word.upper())  # только печатает, НЕ МЕНЯЕТ СЛОВО!
print(word)

# 3. 

#print('Учебное заведение, в котором вы учитесь')
print(questions[word])

while '*' in zvezdochki:  # пока есть неоткрытые буквы
    print(''.join(zvezdochki))  # join - это split наоборот - склеить строку
    user_answer = input('Введите букву или слово целиком: ')
    # Пользователь что-то ввел....
    # word       = 'Академия'
    # zvezdochki = '********'
    if len(user_answer) > 1:
        if user_answer.lower() != word.lower():
            print('Нет, неправильно')
        else:
            print('Вы угадали!')
            zvezdochki = list(word)
    else:
        if user_answer.lower() in word.lower():
            print('Есть такая буква в этом слове!')
        else:
            print('Нет такой буквы')
        for i in range(len(word)):
            if user_answer.lower() == word[i].lower():  # допустим, 'а'

                # НЕТ ЛОЖНОЙ ВЕТКИ ВЕТВЛЕНИЯ! ДОБАВИТЬ!
                
                ##############################
                #                            #
                #      НА КАКОЙ ПОЗИЦИИ?     #
                #                            #
                ##############################

                'Академия'
                'а*а*****'
                # вписано вручную! Не зависит от введенной буквы! ИССПРАВИТЬ!
                # И ПОЗИЦИЮ - ТОЖЕ!
                #zvezdochki[0] = 'а'
                #zvezdochki[2] = 'a'
                zvezdochki[i] = user_answer

print('Вы выиграли в этой игре!')
# Можно усложнить игру, добавив ограничение по количеству попыток

