from datetime import datetime

class Human:

    #               0     1         2
    def __init__(self, name, birthday):  # Метод - фунцкия в классе
        self.__name = name               # Поле - переменная в классе
        self.__birthday = birthday
    
    # Декоратор, превращающий метод в свойство, которое ведет себя подобно полю
    @property
    def age(self):
        print('Тут вообще-то работает функция!')
        return datetime.now().year - self.__birthday.year


h = Human('Wera', datetime(1986, 8, 6))
#print('Дата рождения', h.__birthday)
# ЕСТЬ способ получить доступ к "приватному" полю
# print('Дата рождения', h._Human__birthday)
# Не надо так делать, мы же "прячем" (инкапсулируем) поля для своего удобства...
print('Возраст', h.age)  # Выглядит, как поле, а на деле - вызывает функцию-получатель (getter)
# print('Возраст', h.age())
# Наличие @property без @age.setter ЗАПРЕЩАЕТ запись!
# h.age = 18  # property 'age' of 'Human' object has no setter
# h.birthday = 'Большой секрет'
# print('День рождения', h.birthday)
