import pygame
import time

H = 600
W = 500
FIELD_H = W - 50
FIELD_W = H - 150
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
display.fill(BACKGROUND_COLOR)
field_sub = pygame.Surface((FIELD_W, FIELD_H))
field_sub.fill(BACKGROUND_COLOR)
field_rect = field_sub.get_rect()
field_rect.center = (W // 2, H // 2 + 50)
pygame.draw.line(field_sub, BLACK, (FIELD_W // 3, 0), (FIELD_W // 3, FIELD_H), 3)
pygame.draw.line(field_sub, BLACK, (2 * FIELD_W // 3, 0), (2 * FIELD_W // 3, FIELD_H), 3)
pygame.draw.line(field_sub, BLACK, (0, FIELD_H // 3), (FIELD_W, FIELD_H // 3), 3)
pygame.draw.line(field_sub, BLACK, (0, 2 * FIELD_H // 3), (FIELD_W, 2 * FIELD_H // 3), 3)


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
                time.sleep(2)
            return m[0][i]
        elif m[i][0] == m[i][1] == m[i][2]:
            if m[i][0] != 0:
                pygame.draw.line(field_sub, RED, (l // 2, l // 2 + l * i), (l // 2 + 2 * l, l // 2 + l * i), 5)
                show(m[i][0], m)
                time.sleep(2)
            return m[i][0]
        elif m[0][0] == m[1][1] == m[2][2]:
            if m[0][0] != 0:
                pygame.draw.line(field_sub, RED, (l // 2, l // 2), (l // 2 + 2 * l, l // 2 + 2 * l), 5)
                show(m[0][0], m)
                time.sleep(2)
            return m[0][0]
        elif m[0][2] == m[1][1] == m[2][0]:
            if m[0][2] != 0:
                pygame.draw.line(field_sub, RED, (l // 2 + 2 * l, l // 2 + 2 * l), (l // 2, l // 2),  5)
                show(m[0][2], m)
                time.sleep(2)
            return m[0][2]
    return 0


def show(player, m):
    """Отображает текущее состояние поля"""
    display.fill(BLACK)
    display.blit(field_sub, field_rect)
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
    # print("ходит игрок", player + 1)


def startgame():
    """Запускает игру,
        игрок ставит крестик или нолик в свободную клетку,
        проверяется на наличие закрытой линии,
    """
    game_run = True

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
    print(f"Игра завершена \nпобедил {win(field)} игрок")


if __name__ == "__main__":
    startgame()
