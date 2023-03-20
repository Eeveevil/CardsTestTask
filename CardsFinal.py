import random

deck = [(color, rank) for color in ['R', 'G', 'B', 'W'] for rank in range(1, 11)]

def start(n, c):
    if n*c > len(deck):
        print("Ошибка: недостаточно карт в колоде для раздачи")
        return
    random.shuffle(deck)
    hands = [deck[i*n:(i+1)*n] for i in range(c)]
    for i, hand in enumerate(hands):
        globals()[f"player_{i+1}"] = hand

def get_cards(c):
    try:
        hand = globals()[f"player_{c}"]
    except KeyError:
        print("Ошибка: игрок с данным номером не существует")
        return
    print(f"{c} {' '.join([color+str(rank) for color, rank in hand])}")

while True:
    command = input("Введите команду: ").split()
    if command[0] == 'start':
        try:
            n = int(command[1])
            c = int(command[2])
        except (IndexError, ValueError):
            print("Ошибка: некорректные входные данные")
            continue
        start(n, c)
    elif command[0] == 'get-cards':
        try:
            c = int(command[1])
        except (IndexError, ValueError):
            print("Ошибка: некорректные входные данные")
            continue
        get_cards(c)
    else:
        print("Ошибка: неизвестная команда")