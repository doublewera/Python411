# 1. Написать функцию, которая вычисляет площадь квартиры.
#    Квартира - массив пар "ширина, длина" для каждой комнаты.
# 2. Написать функцию, которая вычисляет площадь квартиры. 
#    Квартира - массив словарей {"ширина": 5, "длина": 3}
# 3. * сложное: Написать функцию, которая делит квартиры на
#    1,2,3-х комнатные. Какая структура данных нам подойдёт?
# 4. Сохранить результаты в файл.

class Room:

    def __init__(self, w, l, h=2.5):
        self.__width = w
        self.__length = l
        self.__height = h

    def area(self):
        return self.__width * self.__length
    
    def __str__(self):
        return f'Комната имеет размеры: длина = {self.__length}, ширина = {self.__width}'
    
r = Room(3, 6)
print(r)
print('Площадь комнаты: ', r.area())

from word import forms

class Flat:

    def __init__(self, rooms):
        self.__rooms = rooms  # [Room(3, 6), Room(4, 5), Room(1, 2)]

    def area(self):
        result = 0
        for r in self.__rooms:
            result += r.area()
        return result

    def room_number(self):
        return len(self.__rooms)

    def __str__(self):
        result = 'В квартире есть %i ' % len(self.__rooms) + forms(
            len(self.__rooms),
            ('комната', 'комнаты', 'комнат'))
        for r in self.__rooms:
            result += '\n' + str(r)
        return result

def save_to_file(filename, content):
    f = open(filename, mode='w', encoding='utf-8')
    f.write(content)
    f.close()

if __name__ == '__main__':
    f = Flat([Room(3, 6), Room(4, 5), Room(1, 2)])
    print(f)
    save_to_file('flat.txt', str(f))
    print('Площадь квартиры = ' + str(f.area()) + ' метров квадратных ')


