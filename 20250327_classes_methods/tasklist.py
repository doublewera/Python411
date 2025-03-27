from datetime import datetime, timedelta
class Task:  # Класс для хранения информации о задаче, деле, поручении и т.д.

    def __init__(self, description, deadline=datetime.now() + timedelta(1)):
        self.dt             = datetime.now()  # Когда задача была поставлена
        self.deadline       = deadline        # Срок, к которому задачу надо сделать
        self.description    = description     # Описание. Подробное и понятное
        self.done           = False           # Сделана или нет?

    def later(self):  # Функция, которая меняет дедлайн
        self.deadline += timedelta(3)

    def __str__(self):
        # начинается и заканчивается двумя подчеркиваниями
        # называется __str__
        # мы не вызываем ее по имени
        # у нее один параметр - self
        # возвращает строку
        return 'Надо ' + self.description + ' к ' + self.deadline.strftime(
            '%d-%B-%Y')

dress = Task('Сшить джинсовое платье из обрезков')
# self передается по умолчанию сам!
print('Что сделать: ', dress.description)
print('Когда поставлена? ', dress.dt)
print('К какому сроку? ', dress.deadline)
print('Сделано? ', dress.done)

dress.later()
# self передается по умолчанию сам!
print('К какому сроку? ', dress.deadline)

print(dress)
dt = datetime.now()
print(dt)