# Написать программу, которая прибавляет к одному текствому файлу другой
# ИСПОЛЬЗОВАТЬ ФУНКЦИИ

def conc(f1, f2):
    # ВНИМЕНИЕ! В первый файл будет добавлено содержимое второго файла!
    kuda = open(f1, 'a')  # на дозапись!
    otkuda = open(f2)
    for line in otkuda:  # берем по очереди все строки 2 файла
        kuda.write(line)
    kuda.close()
    otkuda.close()

conc('school_test.txt', 'answer_list.txt')