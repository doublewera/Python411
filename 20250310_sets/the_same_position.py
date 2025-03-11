# Задание 3
# Есть три кортежа целых чисел необходимо найти элементы,
# которые есть в каждом из кортежей и находятся
# в каждом из кортежей на той же позиции.

t1 = (1, 3, 5, 7, 9, 0)
t2 = (1, 3, 9, 7)
t3 = (2, 3, 4, 5, 9)

print((
    len(t1),
    len(t2),
    len(t3))
)
minlen = min((
    len(t1),
    len(t2),
    len(t3))
)
print(minlen)
result = []
for i in range(minlen):
    # if t1[i] == t2[i] == t3[i]:
    if t1[i] == t2[i] and t2[i] == t3[i]:
        result.append(t1[i])
        print(i, t1[i])
print(result)
