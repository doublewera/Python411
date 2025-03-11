# Задание 2
# Есть три кортежа целых чисел необходимо
# найти элементы, которые уникальны для каждого списка,

t1 = (1, 2, 3, 4, 1, 2, 3, 4)
t2 = (3, 4, 5, 6)
t3 = (4, 5, 6, 7)

# 1. т.е. в каждом кортеже найти уникальные для него элементы
# ... и что с ними делать?
# например, сформировать их них кортеж уникальных множеств
result = set(t1), set(t2), set(t3)

# ...или?
# напечатать их на экран, каждый в отдельной строке
print(set(t1))

print(set(t2))

print(set(t3))

# 2. т.е. найти элементы, которые есть в этом кортеже и нету в других

# Циклом

result = []
for elem in t1:
    if not (elem in t2) and not (elem in t3):
        result.append(elem)
#print(result)
for elem in t2:
    if not (elem in t1) and not (elem in t3):
        result.append(elem)
for elem in t3:
    if not (elem in t1) and not (elem in t2):
        result.append(elem)
print(set(result))

# Формулой

r1 = set(t1) ^ set(t2)
print(' 1 ^ 2 ', r1)
r2 = (set(t1) & set(t2) & set(t3)) ^ set(t3)
print(' (1 & 2 & 3) ^ 3', r2)
print(r1 ^ r2)
