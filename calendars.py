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
            if (month_number + 1) in [4, 6, 9, 11]:
                # Апрель, Июнь, Сентябрь, Ноябрь
                months.append(Month(month_name, 30))
            elif month_number + 1 == 2:
                if self.__year.is_leap_year():
                    # Високосный Февраль
                    months.append(Month(month_name, 29))
                else:
                    # Невисокосный Февраль
                    months.append(Month(month_name, 28))
            else:
                months.append(Month(month_name, 31))
        return months


    def display_calendar(self):
        print(f"Календарь на {self.__year.year} год:")
        # self.__year.year = 525
        for month in self.__months:
            print(month)

c = Calendar(2024)
c.display_calendar()