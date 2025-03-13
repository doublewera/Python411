f = open('tasklist.txt', encoding='utf-8')
header = f.readline()  # в любой момент из открытого файла можно прочитать до конца строки
# Файл можно перебирать по строчкам!
my_tasks = []
for line in f:
    my_tasks.append(line[4:-1])
# Срез (slice) - 
# [откуда,докуда,шаг]
# докуда и шаг - необязательные
# если "докуда" не указано - будет до последнего элемента включительно
# если шаг не указан, будет каждый элемент
print("ГЛАВНОЕ ДЕЛО: ", header)
for elem in my_tasks:
    print(elem)
print(my_tasks)