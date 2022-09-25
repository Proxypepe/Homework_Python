import sqlite3


def add_user(
        connection: sqlite3.Connection,
        cursor: sqlite3.Cursor,
        username: str,
        password: str
):
    insert_user_query = f'''
        INSERT INTO users (name, password) VALUES ( ?, ?)
    '''
    cursor.execute(insert_user_query, (username, password))
    connection.commit()


if __name__ == '__main__':
    conn = sqlite3.connect('my.db')
    c = conn.cursor()
    name = input("Enter username: ")
    password = input("Enter password: ")
    add_user(conn, c, name, password)
    print('\n')
    c.execute('SELECT * FROM users')
    row = c.fetchone()

    while row is not None:
        print(f'id: {row[0]}\n'
              f'login: {row[1]} | Password: {row[2]}')
        row = c.fetchone()
    c.close()
    conn.close()
