def inputPlayer(player, m):
    """Обработка введёных координат """
    while True:
        a = input('Введите координаты через пробел: ').split()
        if len(a) != 2:
            print('координаты введены неверно')
            continue
        b, a = a[1], a[0]

        if not a.isdigit() and not b.isdigit():
            print("координаты введены неверно")
            continue
        a, b = int(a), int(b)
        if (a >= 1) and (a <= 3) and (b >= 1) and (b <= 3):
            a, b = a - 1, b - 1
            if m[a][b] == 0:
                m[a][b] = player + 1
                return m
        print("координаты введены неверно")


def win(m):
    """Проверяет выиграл ли игрок"""
    for i in range(3):
        if m[0][i] == m[1][i] == m[2][i]:
            return m[0][i]
        if m[i][0] == m[i][1] == m[i][2]:
            return m[i][0]
        if m[0][0] == m[1][1] == m[2][2]:
            return m[0][0]
        if m[0][2] == m[1][1] == m[2][0]:
            return m[0][2]
    return 0


def show(player, m):
    """Отображает текущее состояние поля"""
    for i in m:
        print(*i)
    print("ходит игрок", player + 1)


def startgame():
    """Запускает игру,
        игрок ставит крестик или нолик в свободную клетку,
        проверяется на наличие закрытой линии,
    """
    m = [[0] * 3 for _ in range(3)]
    player = 0
    while win(m) == 0:
        show(player, m)
        inputPlayer(player, m)
        player = int(not player)    # смена хода
    print(f"Игра завершена \nпобедил {win(m)} игрок")


if __name__ == "__main__":
    startgame()
