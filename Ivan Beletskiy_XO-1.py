print()
print("Друзья, давайте поиграем в самую классую игру:\n"
"Крестики-Нолики! \n"
    "Ходы делаем так: вводим соответствующие цифры от 1 до 9.\n"
"ПОЕХАЛИ:")
print()
# намечаем поле
maps = [1,2,3,
        4,5,6,
        7,8,9]

# выводим поле в консоль
def print_maps(maps):
    print(maps[0], maps[1], maps[2])
    print(maps[3], maps[4], maps[5])
    print(maps[6], maps[7], maps[8])

# выигрышные комбинации и проверки по ним
def winner_check(maps):
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_comb:
        if maps[i[0]] == maps[i[1]] == maps[i[2]]:
            return maps[i[0]]

# спрашиваем ход у игрока - он меняется с Х на 0
def move_take(player):
    res = False
    while not res:
        take_answer = input("Сейчас ходит " + player + ":")
        try:
            take_answer = int(take_answer)
        except:
            print("ОШИБКА! Вы уверены, что ввели число?") # сразу исключаем возможные неверные символы
            continue
        # проверка диапазона ввода чисел и проверка состояния клетки перед вводом
        if take_answer >= 1 and take_answer <= 9:
            if (str(maps[take_answer - 1]) not in "XO"):
                maps[take_answer - 1] = player
                res = True
            else:
                print("Эта клетка ЗАНЯТА!")
        else:
            print("Вне диапазона! Введите число от 1 до 9:")

# основной игровой цикл
def game(maps):
    counter = 0  # счетчик ходов и поочередная смена игроков
    while True:
        print_maps(maps)
        counter += 1
        if counter % 2 == 1:
            move_take("X")
        else:
            move_take("O")
        #проверка на победу
        if counter > 4:
            win = winner_check(maps)
            if win:
                print(win, "ПОБЕДИЛ!")
                break
        if counter == 9:
            print("НИЧЬЯ!")
            break
    print_maps(maps)

game(maps)
print('Для новой игры нажмите зелёный треугольник вверху')