import sqlite3


def main():
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE
        )
    """)
    conn.commit()

    user_data = ("Alice Smith", "alice@example.com")
    cursor.execute("""
        INSERT INTO users (name, email)
        VALUES (?, ?)
    """, user_data)
    conn.commit()

    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()
    for row in all_users:
        print(f'ID: {row[0]}, name: {row[1]}, email: {row[2]}')

    conn.close()


if __name__ == "__main__":
    main()
