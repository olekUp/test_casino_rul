import sqlite3

db = sqlite3.connect("test_casino.db")
cur = db.cursor()  #створення таблички бд

cur.execute("""CREATE TABLE IF NOT EXISTS user_casino_test (
        user_name TEXT,
        password TEXT,
        cash BIGINT
)  """)
db.commit()


def reg():
    user_login = input("Login: ")
    user_password = input("Password: ")

    cur.execute("SELECT user_name FROM user_casino_test WHERE user_name = ?", (user_login,)) #кортеж
    if cur.fetchone() is None:
        cur.execute(f"INSERT INTO user_casino_test VALUES (?, ?, ?)", (user_login, user_password, 10000))
        db.commit()
        print("Реєстрація пройдена, вітаємо в грі!")
    else:
        print("Раді знову вас бачити")
        for value in cur.execute("SELECT user_name FROM user_casino_test"):
            print(value)


# Функція що повертає з бд кількість грошей певного гравця
def get_cash(userlogin):
    cur.execute("SELECT cash FROM user_casino_test WHERE user_name = ?", (userlogin,))
    res = cur.fetchone()[0] # !!!!
    return res



# Функція оновлення даних гравця кількості грошей
def update_cash(userlogin, new_cash):
    cur.execute("UPDATE user_casino_test SET cash = ? WHERE user_name = ?", (new_cash, userlogin))
    db.commit()

# print(get_cash("Olek"))


