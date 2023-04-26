import pygame

pygame.init()
H = 600
W = 500
FIELD_H = 450
FIELD_W = 450
FPS = 30

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BACKGROUND_COLOR = (255, 204, 102)

display = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game")

# создание поля
field_sub = pygame.Surface((FIELD_W, FIELD_H))
field_rect = field_sub.get_rect()
field_rect.center = (W // 2, H // 2 + 50)

text_sub = pygame.Surface((450, 120))
text_rect = (240, 50)

font = pygame.font.SysFont('arial', 60)
text1 = font.render("Ходят X", True, BLACK, BACKGROUND_COLOR)
text2 = font.render("Ходят O", True, BLACK, BACKGROUND_COLOR)
text3 = font.render("Победил X", True, BLACK, BACKGROUND_COLOR)
text4 = font.render("Победил O", True, BLACK, BACKGROUND_COLOR)
text5 = font.render("Ничья", True, BLACK, BACKGROUND_COLOR)


def draw_field():
    display.fill(BACKGROUND_COLOR)
    field_sub.fill(BACKGROUND_COLOR)
    pygame.draw.line(field_sub, BLACK, (FIELD_W // 3, 0), (FIELD_W // 3, FIELD_H), 5)
    pygame.draw.line(field_sub, BLACK, (2 * FIELD_W // 3, 0), (2 * FIELD_W // 3, FIELD_H), 5)
    pygame.draw.line(field_sub, BLACK, (0, FIELD_H // 3), (FIELD_W, FIELD_H // 3), 5)
    pygame.draw.line(field_sub, BLACK, (0, 2 * FIELD_H // 3), (FIELD_W, 2 * FIELD_H // 3), 5)


def inputPlayer(player, m, pos):
    """Обработка координат, куда нажали"""
    l = FIELD_W // 3
    if m[pos[1] // l][pos[0] // l] == 0:
        m[pos[1] // l][pos[0] // l] = player + 1
        player = int(not player)
    return m, player


def win(m):
    """Проверяет выиграл ли игрок"""
    l = FIELD_W // 3
    for i in range(3):
        if m[0][i] == m[1][i] == m[2][i]:
            if m[0][i] != 0:
                pygame.draw.line(field_sub, RED, (l // 2 + l * i, l // 2), (l // 2 + l * i, l // 2 + l * 2), 5)
                show(m[0][i], m)
            return m[0][i]
        elif m[i][0] == m[i][1] == m[i][2]:
            if m[i][0] != 0:
                pygame.draw.line(field_sub, RED, (l // 2, l // 2 + l * i), (l // 2 + 2 * l, l // 2 + l * i), 5)
                show(m[i][0], m)
            return m[i][0]
        elif m[0][0] == m[1][1] == m[2][2]:
            if m[0][0] != 0:
                pygame.draw.line(field_sub, RED, (l // 2, l // 2), (l // 2 + 2 * l, l // 2 + 2 * l), 5)
                show(m[0][0], m)
            return m[0][0]
        elif m[0][2] == m[1][1] == m[2][0]:
            if m[0][2] != 0:
                pygame.draw.line(field_sub, RED, (l // 2, l // 2 + 2 * l), (l // 2 + 2 * l, l // 2), 5)
                show(m[0][2], m)
            return m[0][2]
        elif sum([row.count(0) for row in m]) == 0:
            return 3
    return 0


def show(player, m):
    """Отображает текущее состояние поля"""
    display.fill(BACKGROUND_COLOR)
    display.blit(field_sub, field_rect)

    text_sub.fill(BACKGROUND_COLOR)
    if player == 1:
        text_sub.blit(text2, text2.get_rect(center=text_rect))
    else:
        text_sub.blit(text1, text1.get_rect(center=text_rect))
    display.blit(text_sub, text_sub.get_rect(center=text_rect))

    for i in range(3):
        for j in range(3):
            if m[i][j] == 1:  # отрисовка крестиков
                l = FIELD_W // 3
                pygame.draw.line(field_sub, BLACK, (15 + l * j, 15 + l * i), ((l - 15) + l * j, (l - 15) + l * i), 10)
                pygame.draw.line(field_sub, BLACK, (15 + l * j, (l - 15) + l * i), ((l - 15) + l * j, 15 + l * i), 10)
            elif m[i][j] == 2:  # отрисовка ноликов
                l = FIELD_W // 3
                pygame.draw.circle(field_sub, BLACK, (l // 2 + l * j, l // 2 + l * i), (l // 2 - 10), 7)

    pygame.display.update()


def endGame(winner):
    text_sub.fill(BACKGROUND_COLOR)
    if winner == 1:
        text_sub.blit(text3, text3.get_rect(center=text_rect))
    elif winner == 2:
        text_sub.blit(text4, text4.get_rect(center=text_rect))
    else:
        text_sub.blit(text5, text5.get_rect(center=text_rect))

    display.blit(text_sub, text_sub.get_rect(center=(250, 50)))
    pygame.display.update()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    startGame()


def startGame():
    """Запускает игру,
        игрок ставит крестик или нолик в свободную клетку,
        проверяется на наличие закрытой линии,
    """
    draw_field()
    field = [[0] * 3 for _ in range(3)]
    player = 1
    while win(field) == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if field_rect.collidepoint(pygame.mouse.get_pos()):
                        mouse_pos = pygame.mouse.get_pos()
                        mouse_pos = (mouse_pos[0] - field_rect.left, mouse_pos[1] - field_rect.top)
                        field, player = inputPlayer(player, field, mouse_pos)
        show(player, field)
        clock.tick(FPS)

    show(player, field)
    endGame(win(field))


if __name__ == "__main__":
    startGame()
