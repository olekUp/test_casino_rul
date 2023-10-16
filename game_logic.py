from test_sql import get_cash, update_cash, reg, cur
import random

# Ігрове поле
matrix_split = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12],
                [13, 14, 15],
                [16, 17, 18],
                [19, 20, 21],
                [22, 23, 24],
                [25, 26, 27],
                [28, 29, 30],
                [31, 32, 33],
                [34, 35, 36]]

# Всі значення ігрового колеса
roulette_wheel = {
    "0": {"color": "зелений", "type": "нуль"},
    "1": {"color": "червоний", "type": "непарне"},
    "2": {"color": "чорний", "type": "парне"},
    "3": {"color": "червоний", "type": "непарне"},
    "4": {"color": "чорний", "type": "парне"},
    "5": {"color": "червоний", "type": "непарне"},
    "6": {"color": "чорний", "type": "парне"},
    "7": {"color": "червоний", "type": "непарне"},
    "8": {"color": "чорний", "type": "парне"},
    "9": {"color": "червоний", "type": "непарне"},
    "10": {"color": "чорний", "type": "парне"},
    "11": {"color": "червоний", "type": "непарне"},
    "12": {"color": "чорний", "type": "парне"},
    "13": {"color": "червоний", "type": "непарне"},
    "14": {"color": "чорний", "type": "парне"},
    "15": {"color": "червоний", "type": "непарне"},
    "16": {"color": "чорний", "type": "парне"},
    "17": {"color": "червоний", "type": "непарне"},
    "18": {"color": "чорний", "type": "парне"},
    "19": {"color": "червоний", "type": "непарне"},
    "20": {"color": "чорний", "type": "парне"},
    "21": {"color": "червоний", "type": "непарне"},
    "22": {"color": "чорний", "type": "парне"},
    "23": {"color": "червоний", "type": "непарне"},
    "24": {"color": "чорний", "type": "парне"},
    "25": {"color": "червоний", "type": "непарне"},
    "26": {"color": "чорний", "type": "парне"},
    "27": {"color": "червоний", "type": "непарне"},
    "28": {"color": "чорний", "type": "парне"},
    "29": {"color": "червоний", "type": "непарне"},
    "30": {"color": "чорний", "type": "парне"},
    "31": {"color": "червоний", "type": "непарне"},
    "32": {"color": "чорний", "type": "парне"},
    "33": {"color": "червоний", "type": "непарне"},
    "34": {"color": "чорний", "type": "парне"},
    "35": {"color": "червоний", "type": "непарне"},
    "36": {"color": "чорний", "type": "парне"},
    "37": {"color": "червоний", "type": "непарне"},
}


# Перевірка ставки на конкретне число
def straight_up(rate, num, username):
    user_cash = get_cash(username)
    if user_cash is not None:
        ball = random.choice(list(roulette_wheel.keys()))
        user_cash -= rate
        if int(ball) == num:
            user_cash += rate * 35
            print(
                f"Вітаю {ball}, {roulette_wheel[ball]['color']} ваш вийграш становить - {rate * 36}\nваш баланс {user_cash} \n")
        else:
            print(f"{ball}  Наступного разу пощастить, ваш баланс {user_cash} \n")
    update_cash(username, user_cash)


# перевірка правильності ставки по правилам split
def check_rate_split(matrix, num1, num2):
    index1 = None
    index2 = None
    # знаходимо індекси нашо1 ставки
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == num1:
                index1 = (i, j)
            elif matrix[i][j] == num2:
                index2 = (i, j)

    row1, col1 = index1
    row2, col2 = index2

    if (
            (row2 - row1 == 1 and col2 == col1) or
            (row2 == row1 and col2 - col1 == 1)
    ):
        return True
    return False


# Перевірка ставки split
def split(rate, num1, num2, username):
    user_cash = get_cash(username)
    ball = random.choice(list(roulette_wheel.keys()))
    if check_rate_split(matrix_split, num1, num2):
        user_cash -= rate
        if num1 == int(ball) or num2 == int(ball):
            user_cash += rate * 17
            print(
                f"Вітаю {ball, roulette_wheel[ball]['color']}ваш вийграш становить - {rate * 17}\nваш баланс {user_cash}")
        else:
            print(f"{ball}  Наступного разу пощастить, ваш баланс {user_cash}")

    update_cash(username, user_cash)


def casino():
    user_login = input("Log in: ")
    cur.execute(" SELECT user_name FROM user_casino_test WHERE user_name = ?", (user_login,))

    if cur.fetchone() is None:
        print("Вітаємо новий гравець, зареєструйся і почни грати")
        reg()
    else:
        print("Раді вас бачити! Гарної гри:)")
        while True:
            answer = input("Оберіть вид стаки: \n1.straight_up  \n2.split  \n3.exit \n")
            if answer == "exit":
                print(f"Непогана гра, чакаємо вас знову!\n")
                break
            elif answer == "1":
                rate = int(input("Ведіть суму ставки: "))
                choice = int(input("Оберіть число на яке хочете поставити: "))
                straight_up(rate, choice, user_login)
            elif answer == "2":
                rate = int(input("Ведіть суму ставки: "))
                num_1, num_2 = list(map(int, input("Оберіть числа на які хочете поставити через пробіл: ").split()))
                if check_rate_split(matrix_split, num_1, num_2):
                    split(rate, num_1, num_2, user_login)
                else:
                    print("Невірна ставка, спробуй ще раз ")
                    continue
