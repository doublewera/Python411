# написать программу, которая из файла ответов читает и записывает в словарь
# ключи - вопросы, значения - верные ответы

def load_from_file(fn):  # передадим ей имя файла
    #f = open(fn, encoding='utf-8')
    #f.close()
    res = {}
    with open(fn, encoding='utf-8') as f:  # плохо для try!!!
        for line in f:
            if ' верно' in line:
                question, answer = line.split(' = ')
                res[question] = answer[:-7]  # отрезали " верно\n"
            else:
                question, answers = line.split(' = ')
                wrong, answer = answers.split(' неверно, правильный ответ ')
                res[question] = answer.strip()
    return res

print(load_from_file('school_test.txt'))