def get_raw_data():
    import psycopg

    # Подключиться к БД

    conn = psycopg.connect(
        dbname='students',
        user='wera',
    )
    print(conn)
    cursor = conn.cursor()

    # Прочитать

    cursor.execute('SELECT first_name, row_number, comp FROM group411')  # ; не обязательна в отличие от консоли!
    # Достать сразу все данные из запроса
    data = cursor.fetchall()

    # Отключиться
    cursor.close()
    conn.close()
    return data

def understand(data):
    max_name = 10
    print(data)
    students = [[None, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None]]
    for s in data:
        name, row, comp = s
        if row:
            students[4 - row][comp - 1] = name

    return students, max_name

def draw(classroom, max_name):
    line = '+' + 4 * ('-' * max_name + '+')
    print(line)
    for row in classroom:
        row_str = '|'
        for chair in row:
            if chair:
                row_str += ('%%%is' % max_name) % chair + '|'
            else:
                row_str += ' ' * max_name + '|'
        print(row_str)
        print(line)

def update(name, row, comp):
    import psycopg

    # Подключиться к БД

    conn = psycopg.connect(
        dbname='students',
        user='wera',
    )
    cursor = conn.cursor()

    # Записать и подтвердить

    cursor.execute("UPDATE group411 SET row_number=%i, comp=%i WHERE first_name='%s'" % (
        row, comp, name  # Если имена повторяются, будет неправильная БД!
    ))  # ; не обязательна в отличие от консоли!
    conn.commit()  # Подтвердить изменения

    # Отключиться
    cursor.close()
    conn.close()

update('Андрей', 1, 2)
draw(
    *understand(
        get_raw_data()))


