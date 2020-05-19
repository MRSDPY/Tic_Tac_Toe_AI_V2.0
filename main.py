import random
from math import inf as infinite

board_ = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

player_ = ["X", "O"]
ai_ = None
human = None
current = None
count = 0


def board():
    print("\n")
    for i in range(len(board_)):
        for j in range(0, 3):
            print(board_[i][j], "\t", end="")
        print("\n")


def turn():
    global current
    # try:
    if current == ai_:
        ai_turn()
        current = select_p(current)
    else:
        row = (int(input("Enter row in between [1-3] : ")) - 1)
        column = (int(input("Enter column in between [1-3] : ")) - 1)
        if board_[row][column] == '-' and row in range(0, 3) and column in range(0, 3):
            board_[row][column] = current
            current = select_p(current)
        else:
            print("Please Enter Valid Number")


# except Exception as e:
#     print("You can enter number between 1 to 3 and only enter numbers.", e)


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


def play_game():
    while True:
        board()
        global count, current
        fist = board_[0].count('-')
        sec = board_[1].count('-')
        thir = board_[2].count('-')
        count = fist + sec + thir

        if current == None:
            select_p()

        print("AI = ", ai_, "  HUMAN = ", human)
        turn()

        rs = check_winner(board_)

        if rs == ai_:
            board()
            print(f"{ai_} is won the game.")
            break
        elif rs == human:
            board()
            print(f"{human} is won the game..")
            break
        elif rs == 'tie':
            board()
            print(f"Tie between both 'X' and 'O' player")
            break
        else:
            continue


play_game()
