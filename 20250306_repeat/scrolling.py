# Как просмотреть весь список, множество или кортеж?
# Поэлементно

fruit = {'apple', 'orange', 'avocado'}
for f in fruit:  # for (let elem of list) {........}
    print(f)
    print('Длина слова ', f, 'равна', len(f))

# По позиции (тупой, но распространённый вариант)

fruit = ('apple', 'orange', 'avocado')
for i in range(len(fruit)):
    print(i, fruit[i])

# По позиции - супермодный варинат
fruit = ('apple', 'orange', 'avocado')
for i, f in enumerate(fruit):
    print(i, f)

