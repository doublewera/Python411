class DateTime: #   0     1      2      3       4         5         6
    def __init__(self, year, month=1, day=1, hour=0, minute=0, second=0):
# инициализатор с параметрами; =1, =0 - значения по умолчанию
# то же самое есть и у функций. Если мы не передали параметр, будет 
# использовано значение по умолчанию.
# Если мы передали параметр, будет использовано ПЕРЕДАННОЕ НАМИ значение
        self.year   = year
        self.month  = month
        self.day    = day
        self.hour   = hour
        self.minute = minute
        self.second = second

dt = DateTime(2025)
print(dt.hour, dt.month)
dt_future = DateTime(2026, 5, 16)
print(dt_future.hour, dt_future.month)