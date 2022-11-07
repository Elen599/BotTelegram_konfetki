from random import randrange


def calculator(num):
    global balance
    balance -= num
    text = f"Конфет осталось {balance}\n"
    if balance > 0:
        text += bot_calculator()
        return text
    else:
        return "Ты победил"


def bot_calculator():
    global balance
    while True:
        box = randrange(1, 11)
        if box <= balance:
            break
    balance -= box
    if balance < 1:
        return "Победил Бот, взяв оставшиеся конфеты"
    else:
        text = f"Бот взял {box}\nКонфет осталось {balance}\nТеперь бери ты"
        return text


balance = 50