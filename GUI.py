import pygame
import sys
import random
from math import inf as infinite

pygame.init()

player_ = ["X", "O"]
ai_ = None
human = None
current = None
error = False
count = 0

width = 600
height = 600

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

game_status = True

font = pygame.font.Font('Font/Roboto-Black.ttf', 80)
dic_res = {1: [(0, 0), (200, 200)], 2: [(200, 0), (400, 200)], 3: [(400, 0), (600, 200)],
           4: [(0, 200), (200, 400)], 5: [(200, 200), (400, 400)], 6: [(400, 200), (600, 400)],
           7: [(0, 400), (200, 600)], 8: [(200, 400), (400, 600)], 9: [(400, 400), (600, 600)]}
col = None
row = None
mouse_x = None
mouse_y = None
board_ = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]


def select_p(player=None):
    global current, player_, ai_, human
    if player == None:
        human = player_[random.randint(0, 1)]
        current = human
        if player_[player_.index(human)] == 'X':
            ai_ = 'O'
        else:
            ai_ = 'X'
        return current
    else:
        if player == human:
            current = ai_
        else:
            current = human
        return current


def ai_turn():
    global current
    best_score = -infinite
    best_move = []

    for i in range(3):
        for j in range(3):
            if board_[i][j] == "-":
                board_[i][j] = ai_
                score = minimax(board_, 0, False)
                board_[i][j] = "-"
                if score > best_score:
                    best_score = score
                    best_move.append([i, j])

    board_[best_move[-1][0]][best_move[-1][1]] = current


def minimax(board_, depth, isai):
    winner_result = check_winner(board_)

    if winner_result is not None:
        if winner_result == ai_:
            return 1
        elif winner_result == human:
            return -1
        else:
            return 0

    if isai:
        bestscore = -infinite
        for i in range(3):
            for j in range(3):
                if board_[i][j] == "-":
                    board_[i][j] = ai_
                    score = minimax(board_, depth + 1, False)
                    board_[i][j] = "-"
                    bestscore = max(score, bestscore)
        return bestscore
    else:
        bestscore = infinite
        for i in range(3):
            for j in range(3):
                if board_[i][j] == "-":
                    board_[i][j] = human
                    score = minimax(board_, depth + 1, True)
                    board_[i][j] = "-"
                    bestscore = min(score, bestscore)
        return bestscore


def check_winner(bb3):
    # check horizontal
    if bb3[0][0] == bb3[0][1] == bb3[0][2] != '-':
        return ai_ if bb3[0][0] == ai_ else human

    if bb3[1][0] == bb3[1][1] == bb3[1][2] != '-':
        return ai_ if bb3[1][0] == ai_ else human

    if bb3[2][0] == bb3[2][1] == bb3[2][2] != '-':
        return ai_ if bb3[2][0] == ai_ else human

    # check vertical
    if bb3[0][0] == bb3[1][0] == bb3[2][0] != '-':
        return ai_ if bb3[0][0] == ai_ else human

    if bb3[0][1] == bb3[1][1] == bb3[2][1] != '-':
        return ai_ if bb3[0][1] == ai_ else human

    if bb3[0][2] == bb3[1][2] == bb3[2][2] != '-':
        return ai_ if bb3[0][2] == ai_ else human

    # check for cross
    if bb3[0][0] == bb3[1][1] == bb3[2][2] != '-':
        return ai_ if bb3[0][0] == ai_ else human

    if bb3[0][2] == bb3[1][1] == bb3[2][0] != '-':
        return ai_ if bb3[0][2] == ai_ else human

    for i in range(3):
        for j in range(3):
            if bb3[i][j] == "-":
                return None
    else:
        return 'tie'


def draw_circle():
    if board_[0][0] is not "-":
        x = font.render(board_[0][0], True, (0, 0, 0))
        display.blit(x, (
            ((dic_res[1][0][0] + dic_res[1][1][0]) // 2) - 25, ((dic_res[1][0][1] + dic_res[1][1][1]) // 2) - 40))

    if board_[0][1] is not "-":
        x = font.render(board_[0][1], True, (0, 0, 0))
        display.blit(x, (
            ((dic_res[2][0][0] + dic_res[2][1][0]) // 2) - 25, ((dic_res[2][0][1] + dic_res[2][1][1]) // 2) - 40))

    if board_[0][2] is not "-":
        x = font.render(board_[0][2], True, (0, 0, 0))
        display.blit(x, (
            ((dic_res[3][0][0] + dic_res[3][1][0]) // 2) - 25, ((dic_res[3][0][1] + dic_res[3][1][1]) // 2) - 40))

    if board_[1][0] is not "-":
        x = font.render(board_[1][0], True, (0, 0, 0))
        display.blit(x, (
            ((dic_res[4][0][0] + dic_res[4][1][0]) // 2) - 25, ((dic_res[4][0][1] + dic_res[4][1][1]) // 2) - 40))

    if board_[1][1] is not "-":
        x = font.render(board_[1][1], True, (0, 0, 0))
        display.blit(x, (
            ((dic_res[5][0][0] + dic_res[5][1][0]) // 2) - 25, ((dic_res[5][0][1] + dic_res[5][1][1]) // 2) - 40))

    if board_[1][2] is not "-":
        x = font.render(board_[1][2], True, (0, 0, 0))
        display.blit(x, (
            ((dic_res[6][0][0] + dic_res[6][1][0]) // 2) - 25, ((dic_res[6][0][1] + dic_res[6][1][1]) // 2) - 40))

    if board_[2][0] is not "-":
        x = font.render(board_[2][0], True, (0, 0, 0))
        display.blit(x, (
            ((dic_res[7][0][0] + dic_res[7][1][0]) // 2) - 25, ((dic_res[7][0][1] + dic_res[7][1][1]) // 2) - 40))

    if board_[2][1] is not "-":
        x = font.render(board_[2][1], True, (0, 0, 0))
        display.blit(x, (
            ((dic_res[8][0][0] + dic_res[8][1][0]) // 2) - 25, ((dic_res[8][0][1] + dic_res[8][1][1]) // 2) - 40))

    if board_[2][2] is not "-":
        x = font.render(board_[2][2], True, (0, 0, 0))
        display.blit(x, (
            ((dic_res[9][0][0] + dic_res[9][1][0]) // 2) - 25, ((dic_res[9][0][1] + dic_res[9][1][1]) // 2) - 40))


def get_row_col(m_x, m_y):
    if m_x < width / 3:
        col = 1
    elif m_x < width / 3 * 2:
        col = 2
    elif m_x < width:
        col = 3
    else:
        col = None

    if m_y < height / 3:
        row = 1
    elif m_y < height / 3 * 2:
        row = 2
    elif m_y < height:
        row = 3
    else:
        row = None

    return col, row


def draw_grid():
    dis = 600 // 3

    x = 0
    y = 0
    for i in range(width):
        x += dis
        y += dis
        pygame.draw.line(display, [0, 0, 0], (x, 0), (x, 600))
        pygame.draw.line(display, [0, 0, 0], (0, y), (600, y))


while True:
    winner = check_winner(board_)
    fist = board_[0].count('-')
    sec = board_[1].count('-')
    thir = board_[2].count('-')
    count = fist + sec + thir
    print(count)
    if current == None:
        select_p()

    display.fill((255, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = False
            sys.exit()

    if count == 0 or count <= 0 or winner is not None:
        display.fill((0, 0, 0))
        win_font = pygame.font.Font('Font/Roboto-Black.ttf', 50)
        wf = win_font.render(f"{winner}", True, (255, 255, 255))
        display.blit(wf, (width//2, height//2))
    else:
        if current == ai_:
            ai_turn()
            current = select_p(current)
        elif current == human:
            l, m, r = pygame.mouse.get_pressed()
            if l == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col, row = get_row_col(mouse_x, mouse_y)
                if board_[row - 1][col - 1] is "-":
                    board_[row - 1][col - 1] = current
                    current = select_p(current)
                else:
                    print("This Is Filled")
        else:
            pass

    draw_circle()

    draw_grid()
    pygame.display.update()
