def multiplication():
    for i in range(10**8):  # 100 миллионов умножений
        6.9 * 7.3
    print('Долгая функция закончилась')
    return 789

from datetime import datetime, timezone
def measure_time(func):
    dt_start = datetime.now(timezone.utc)
    func()  # вызываем ту функцию, которую мы передали
    dt_end = datetime.now(timezone.utc)
    return dt_end - dt_start

def division():
    print('Начинает работу функция деления. Я 300 тысяч раз разделю 234.6 на 287.2!')
    for i in range(3 * 10**8):
        234.6/287.2
    print('С вами была функция деления. До новых встреч!')

print(measure_time(multiplication))
print(measure_time(division))