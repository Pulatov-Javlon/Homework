def display_board(board):
    print(f"|{board[1]}|{board[2]}|{board[3]}|\n|{board[4]}|{board[5]}|{board[6]}|\n|{board[7]}|{board[8]}|{board[9]}|")
    pass


test_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
display_board(test_board)


def player_input():
    ask_user_number = int(input("Choose a number: "))
    while ask_user_number not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        ask_user_number = int(input("Choose a number: "))
    else:
        if ask_user_number in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            player_choice_type = input("X or O? ")
            if player_choice_type == 'x' or player_choice_type == 'X':
                test_board[ask_user_number] = 'X'
                display_board(test_board)
            elif player_choice_type == 'o' or player_choice_type == 'O':
                test_board[ask_user_number] = 'O'
                display_board(test_board)
    pass


def win_check(board):
    if test_board[1] == 'X' and test_board[2] == 'X' and test_board[3] == 'X':
        print("X gamer is the WINNER")
    elif test_board[1] == 'X' and test_board[4] == 'X' and test_board[7] == 'X':
        print("X gamer is the WINNER")
    elif test_board[2] == 'X' and test_board[5] == 'X' and test_board[8] == 'X':
        print("X gamer is the WINNER")
    elif test_board[3] == 'X' and test_board[6] == 'X' and test_board[9] == 'X':
        print("X gamer is the WINNER")
    elif test_board[7] == 'X' and test_board[8] == 'X' and test_board[9] == 'X':
        print("X gamer is the WINNER")
    elif test_board[7] == 'X' and test_board[5] == 'X' and test_board[3] == 'X':
        print("X gamer is the WINNER")
    elif test_board[7] == 'X' and test_board[5] == 'X' and test_board[3] == 'X':
        print("X gamer is the WINNER")
    elif test_board[4] == 'X' and test_board[5] == 'X' and test_board[6] == 'X':
        print("X gamer is the WINNER")
    elif test_board[1] == 'X' and test_board[5] == 'X' and test_board[9] == 'X':
        print("X gamer is the WINNER")
    elif test_board[3] == 'X' and test_board[5] == 'X' and test_board[7] == 'X':
        print("X gamer is the WINNER")
    elif test_board[1] == 'O' and test_board[2] == 'O' and test_board[3] == 'O':
        print("O gamer is the WINNER")
    elif test_board[1] == 'O' and test_board[4] == 'O' and test_board[7] == 'O':
        print("O gamer is the WINNER")
    elif test_board[2] == 'O' and test_board[5] == 'O' and test_board[8] == 'O':
        print("O gamer is the WINNER")
    elif test_board[3] == 'O' and test_board[6] == 'O' and test_board[9] == 'O':
        print("O gamer is the WINNER")
    elif test_board[7] == 'O' and test_board[8] == 'O' and test_board[9] == 'O':
        print("O gamer is the WINNER")
    elif test_board[7] == 'O' and test_board[5] == 'O' and test_board[3] == 'O':
        print("O gamer is the WINNER")
    elif test_board[7] == 'O' and test_board[5] == 'O' and test_board[3] == 'O':
        print("O gamer is the WINNER")
    elif test_board[4] == 'O' and test_board[5] == 'O' and test_board[6] == 'O':
        print("O gamer is the WINNER")
    elif test_board[1] == 'O' and test_board[5] == 'O' and test_board[9] == 'O':
        print("O gamer is the WINNER")
    elif test_board[3] == 'O' and test_board[5] == 'O' and test_board[7] == 'O':
        print("O gamer is the WINNER")

    pass

while '1' in test_board:
    try:
        player_input()
    except:
        win_check(test_board)
    else:
        win_check(test_board)
        continue


while '2' in test_board:
    try:
        player_input()
    except:
        win_check(test_board)
    else:
        win_check(test_board)
        continue


while '3' in test_board:
    try:
        player_input()
    except:
        win_check(test_board)
    else:
        win_check(test_board)
        continue


while '4' in test_board:
    try:
        player_input()
    except:
        win_check(test_board)
    else:
        win_check(test_board)
        continue

while '5' in test_board:
    try:
        player_input()
    except:
        win_check(test_board)
    else:
        win_check(test_board)
        continue


while '6' in test_board:
    try:
        player_input()
    except:
        win_check(test_board)
    else:
        win_check(test_board)
        continue


while '7' in test_board:
    try:
        player_input()
    except:
        win_check(test_board)
    else:
        win_check(test_board)
        continue


while '8' in test_board:
    try:
        player_input()
    except:
        win_check(test_board)
    else:
        win_check(test_board)
        continue


while '9' in test_board:
    try:
        player_input()
    except:
        win_check(test_board)
    else:
        win_check(test_board)
        continue





