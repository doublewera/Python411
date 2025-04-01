def multiplication():
    for i in range(10**8):  # 100 миллионов умножений
        6.9 * 7.3
    print('Долгая функция закончилась')
    return 789

from datetime import datetime, timezone
def measure_time():
    dt_start = datetime.now(timezone.utc)
    multiplication()
    dt_end = datetime.now(timezone.utc)
    print(dt_end - dt_start)

measure_time()