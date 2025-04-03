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

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def set_length(self, new_length):
        # Сеттер позволяет дополнительно контролировать вводимые данные
        if isinstance(new_length, float) or isinstance(new_length, int):
            self.__length = new_length
        else:
            print("ДЛИНА ДОЛЖНА БЫТЬ ЧИСЛОМ, А НЕ %s" % (new_length)) 

    def area(self):
        return self.__width * self.__length
    
    def __str__(self):
        return f'Комната имеет размеры: длина = {self.__length}, ширина = {self.__width}'
    
r = Room(3, 6)
print(r)
print('Площадь комнаты: ', r.area())
r.set_length(7.5)
print(r)
print('Площадь комнаты: ', r.area())
r.set_length("Очень длинная")
r.length = 