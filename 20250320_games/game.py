import random  # библиотека для случайного выбора

from pole_q import questions  # получение списка вопросов из питонного файла

# 1. Создается загаданное слово, число и т.д. - 
# последовательность символов

# question = # Выбрать вопрос из словаря вопросов
# Найдите в кодах, презентациях и прошлых уроках способ, как выбрать
# случайным образом вопрос и ответ

def get_answer(questions):
    word       = 'Академия'
    word = random.choice(list(questions.keys()))
    return word

def prepare_hint(word):
    zvezdochki = '*' * len(word)  # Python!
    return list(zvezdochki)  # чтобы можно было заменять на буквы!

def diagnostics(word, user_answer, zvezdochki):
    # Если пользователь ввел слово целоком: длина больше 1
    if len(user_answer) > 1:
        # lower(), чтоб можно было ввести маленькими буквами
        if user_answer.lower() != word.lower():
            print('Нет, неправильно')
            return zvezdochki
        else:
            print('Вы угадали!')
            return list(word)
    if len(user_answer) == 0:
        print('Нужно ввести букву!')
        return zvezdochki  
    # else не нужен, если выше был успех или неудача, мы покинем функцию
    if user_answer.lower() in word.lower():
        print('Есть такая буква в этом слове!')
    else:
        print('Нет такой буквы')
    for i in range(len(word)):  # Д
        # 01234567
        # Академия
        # 0 А а
        # 1 к к
        # 2 а а
        # 3 д д Д  - надо заменить звёздочку номер 3 (считая с нуля) на букву д ***д****
        # просматриваем всё слово! Все номера букв в слове!
        if user_answer.lower() == word[i].lower():
            zvezdochki[i] = word[i]  # user_answer
    return zvezdochki


def main():
    # 1. Создается загаданное слово
    word = get_answer(questions)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2. Показать человеку вопрос и звездочки
    print(questions[word])
    # 2. Создается подсказка
    zvezdochki = prepare_hint(word)
    # 3. Пока человек не угадал (пока остались звездочки)
    while '*' in zvezdochki:
    #    3.0 Вывести подсказку
        print(''.join(zvezdochki))  # join - это split наоборот - склеить строку
    #    3.1 принять попытку
        user_answer = input('Введите букву или слово целиком: ')
        zvezdochki = diagnostics(word, user_answer, zvezdochki)

main()
print('Вы выиграли в этой игре!')
# Можно усложнить игру, добавив ограничение по количеству попыток

