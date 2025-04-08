class Year:

    def __init__(self, year):
        self.__year = year

    # свойство - поле, которого "нет", но присваивание и чтение котрого
    # контролируются его геттером и сеттером. Обычно не пишут get, set
    @property  # Этот декоратор позволяет обращаться на чтение к
    def year(self):  #  полю класса по имени функции на чтение
        return self.__year

    def is_leap_year(self):
        # Проверка на високосный год
        return (self.__year % 4 == 0 and self.__year % 100 != 0) or (self.__year % 400 == 0)
    

class Month:

    def __init__(self, name, days):
        self.__name = name
        self.__days = days

    def __str__(self):
        return f"{self.__name}: {self.__days} дней"


class Calendar:
    def __init__(self, year):
        self.__year = Year(year)
        self.__months = self.__create_months()

    def __create_months(self):
        # Создание списка месяцев високосного года
        months = []
        names = [
            "Январь",
            "Февраль",
            "Март",
            "Апрель",
            "Май",
            "Июнь",
            "Июль",
            "Август",
            "Сентябрь",
            "Октябрь",
            "Ноябрь",
            "Декабрь"
        ]
        for month_number, month_name in enumerate(names):
            # enumerate возвращает пары "номер" - "элемент"
            months.append(
                Month(
                    month_name,
                    self.days_in_month(month_number + 1)))
        return months
    
    # Функция, не меняющая поля класса!
    def days_in_month(self, month_number):  # 1..12
        if month_number in [4, 6, 9, 11]:
            # Апрель, Июнь, Сентябрь, Ноябрь
            return 30
        elif month_number == 2:
            if self.__year.is_leap_year():
                # Високосный Февраль
                return 29
            # Невисокосный Февраль
            return 28
        return 31


    def display_calendar(self):
        print(f"Календарь на {self.__year.year} год:")
        # self.__year.year = 525
        for month in self.__months:
            print(month)

c = Calendar(2024)
c.display_calendar()

from datetime import datetime
dt = datetime.now()
#print(dt.year)
#dt.year = 2028
#print(dt)