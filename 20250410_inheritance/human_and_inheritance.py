from datetime import datetime

class Human:

    #               0     1         2
    def __init__(self, name, birthday):  # Метод - фунцкия в классе
        self.__name = name               # Поле - переменная в классе
        self.__birthday = birthday
        # Золотое правило: если вы не знаете, зачем вам публичное поле - сделайте его приватным
    
    # Декоратор, превращающий метод в свойство, которое ведет себя подобно полю
    @property
    def age(self):
        print('Тут вообще-то работает функция!')
        return datetime.now().year - self.__birthday.year
    
    # Сделаем возможность читать и записывать ДР
    @property
    def birthday(self):
        return self.__birthday
    
    # Теперь можно создать метод для записи поля
    @birthday.setter
    def birthday(self, new_birthday):
        # Сеттер управляет присваиванием! Вы можете не допустить присваивание,
        # если оно испортит вам поле
        if isinstance(new_birthday, datetime):
            if new_birthday < datetime.now():
                self.__birthday = new_birthday
            else:
                print('Дата из будущего: ', new_birthday)
        else:
            print('Не является datetime: ', new_birthday, type(new_birthday))

h = Human('Wera', datetime(1986, 8, 6))
#print('Дата рождения', h.__birthday)
# ЕСТЬ способ получить доступ к "приватному" полю
# print('Дата рождения', h._Human__birthday)
# Не надо так делать, мы же "прячем" (инкапсулируем) поля для своего удобства...
print('Возраст', h.age)  # Выглядит, как поле, а на деле - вызывает функцию-получатель (getter)
# print('Возраст', h.age())
# Наличие @property без @age.setter ЗАПРЕЩАЕТ запись!
# h.age = 18  # property 'age' of 'Human' object has no setter

# Поменять - нельзя
#dt = h.birthday
#dt.replace(hour=11)
#h.birthday.replace(hour=11)
h.birthday = 'Большой секрет'
h.birthday = datetime(2029, 6, 3)
h.birthday = datetime(2020, 6, 3)
print('День рождения', h.birthday)


# Унаследовать класс Человек, создав класс "студент".
# У студента есть массив оценок, номер группы и курс.
# Напечатать студента: 
# Вася, группа 1234, Питон, [12, 10, 6, 10, 8, 12, 10]

# class Дочерний(Родительский)

class Student(Human):

    def __init__(self, name, birthday, group, course):
        super().__init__(name, birthday)
        self.__marks = []
        self.__group = group
        self.__course = course


    @property
    def mark(self):
        return self.__marks

    @mark.setter
    def mark(self, new_mark):
        if isinstance(new_mark, int) and 0 < new_mark < 13:
            self.__marks.append(new_mark)


s = Student("Вася", datetime(2000, 1, 1), '411', 'Python')
s.mark = 12
s.mark = 10
s.mark = 6
s.mark = 10
s.mark = 8
print(s.mark)
print(s.age)