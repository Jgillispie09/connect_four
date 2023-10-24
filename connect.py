board = ["-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-"]

player1 = 'O'
player2 = 'X'

def print_board(board):
    print("|" + board[0] + "|" + board [1] + "|" + board[2] + "|" + board[3] + "|" + board[4] + "|" + board[5] + "|" + board[6] + "|")
    print("+-+-+-+-+-+-+-+")
    print("|" + board[7] + "|" + board [8] + "|" + board[9] + "|" + board[10] + "|" + board[11] + "|" + board[12] + "|" + board[13] + "|")
    print("+-+-+-+-+-+-+-+")
    print("|" + board[14] + "|" + board [15] + "|" + board[16] + "|" + board[17] + "|" + board[18] + "|" + board[19] + "|" + board[20] + "|")
    print("+-+-+-+-+-+-+-+")
    print("|" + board[21] + "|" + board [22] + "|" + board[23] + "|" + board[24] + "|" + board[25] + "|" + board[26] + "|" + board[27] + "|")
    print("+-+-+-+-+-+-+-+")
    print("|" + board[28] + "|" + board [29] + "|" + board[30] + "|" + board[31] + "|" + board[32] + "|" + board[33] + "|" + board[34] + "|")
    print("+-+-+-+-+-+-+-+")
    print("|" + board[35] + "|" + board [36] + "|" + board[37] + "|" + board[38] + "|" + board[39] + "|" + board[40] + "|" + board[41] + "|")
    print("---------------")
    print("-1-2-3-4-5-6-7-")

def player1_input():
    while True:
        choice = input("Player One: Where would you like to place your piece? (Enter 1-7): ")
        if choice == '1':
            if board[35] == "-":
                board[35] = player1
                break
            elif board[35] != "-":
                if board[28] == "-":
                    board[28] = player1
                    break
                elif board[28] != "-":
                    if board[21] == "-":
                        board[21] = player1
                        break
                    elif board[21] != "-":
                        if board[14] == "-":
                            board[14] = player1
                            break
                        elif board[14] != "-":
                            if board[7] == "-":
                                board[7] = player1
                                break
                            elif board[7] != "-":
                                if board[0] == "-":
                                    board[0] = player1
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        elif choice == '2':
            if board[36] == "-":
                board[36] = player1
                break
            elif board[36] != "-":
                if board[29] == "-":
                    board[29] = player1
                    break
                elif board[29] != "-":
                    if board[22] == "-":
                        board[22] = player1
                        break
                    elif board[22] != "-":
                        if board[15] == "-":
                            board[15] = player1
                            break
                        elif board[15] != "-":
                            if board[8] == "-":
                                board[8] = player1
                                break
                            elif board[8] != "-":
                                if board[1] == "-":
                                    board[1] = player1
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        elif choice == '3':
            if board[37] == "-":
                board[37] = player1
                break
            elif board[37] != "-":
                if board[30] == "-":
                    board[30] = player1
                    break
                elif board[30] != "-":
                    if board[23] == "-":
                        board[23] = player1
                        break
                    elif board[23] != "-":
                        if board[16] == "-":
                            board[16] = player1
                            break
                        elif board[16] != "-":
                            if board[9] == "-":
                                board[9] = player1
                                break
                            elif board[9] != "-":
                                if board[2] == "-":
                                    board[2] = player1
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        elif choice == '4':
            if board[38] == "-":
                board[38] = player1
                break
            elif board[38] != "-":
                if board[31] == "-":
                    board[31] = player1
                    break
                elif board[31] != "-":
                    if board[24] == "-":
                        board[24] = player1
                        break
                    elif board[24] != "-":
                        if board[17] == "-":
                            board[17] = player1
                            break
                        elif board[17] != "-":
                            if board[10] == "-":
                                board[10] = player1
                                break
                            elif board[10] != "-":
                                if board[3] == "-":
                                    board[3] = player1
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        elif choice == '5':
            if board[39] == "-":
                board[39] = player1
                break
            elif board[39] != "-":
                if board[32] == "-":
                    board[32] = player1
                    break
                elif board[32] != "-":
                    if board[25] == "-":
                        board[25] = player1
                        break
                    elif board[25] != "-":
                        if board[18] == "-":
                            board[18] = player1
                            break
                        elif board[18] != "-":
                            if board[11] == "-":
                                board[11] = player1
                                break
                            elif board[11] != "-":
                                if board[4] == "-":
                                    board[4] = player1
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        elif choice == '6':
            if board[40] == "-":
                board[40] = player1
                break
            elif board[40] != "-":
                if board[33] == "-":
                    board[33] = player1
                    break
                elif board[33] != "-":
                    if board[26] == "-":
                        board[26] = player1
                        break
                    elif board[26] != "-":
                        if board[19] == "-":
                            board[19] = player1
                            break
                        elif board[19] != "-":
                            if board[12] == "-":
                                board[12] = player1
                                break
                            elif board[12] != "-":
                                if board[5] == "-":
                                    board[5] = player1
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        elif choice == '7':
            if board[41] == "-":
                board[41] = player1
                break
            elif board[41] != "-":
                if board[34] == "-":
                    board[34] = player1
                    break
                elif board[34] != "-":
                    if board[27] == "-":
                        board[27] = player1
                        break
                    elif board[27] != "-":
                        if board[20] == "-":
                            board[20] = player1
                            break
                        elif board[20] != "-":
                            if board[13] == "-":
                                board[13] = player1
                                break
                            elif board[13] != "-":
                                if board[6] == "-":
                                    board[6] = player1
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        else:
            print("Invalid Input: Please try again.")
                                
def player2_input():
    while True:
        choice = input("Player Two: Where would you like to place your piece? (Enter 1-7): ")
        if choice == '1':
            if board[35] == "-":
                board[35] = player2
                break
            elif board[35] != "-":
                if board[28] == "-":
                    board[28] = player2
                    break
                elif board[28] != "-":
                    if board[21] == "-":
                        board[21] = player2
                        break
                    elif board[21] != "-":
                        if board[14] == "-":
                            board[14] = player2
                            break
                        elif board[14] != "-":
                            if board[7] == "-":
                                board[7] = player2
                                break
                            elif board[7] != "-":
                                if board[0] == "-":
                                    board[0] = player2
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        elif choice == '2':
            if board[36] == "-":
                board[36] = player2
                break
            elif board[36] != "-":
                if board[29] == "-":
                    board[29] = player2
                    break
                elif board[29] != "-":
                    if board[22] == "-":
                        board[22] = player2
                        break
                    elif board[22] != "-":
                        if board[15] == "-":
                            board[15] = player2
                            break
                        elif board[15] != "-":
                            if board[8] == "-":
                                board[8] = player2
                                break
                            elif board[8] != "-":
                                if board[1] == "-":
                                    board[1] = player2
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        elif choice == '3':
            if board[37] == "-":
                board[37] = player2
                break
            elif board[37] != "-":
                if board[30] == "-":
                    board[30] = player2
                    break
                elif board[30] != "-":
                    if board[23] == "-":
                        board[23] = player2
                        break
                    elif board[23] != "-":
                        if board[16] == "-":
                            board[16] = player2
                            break
                        elif board[16] != "-":
                            if board[9] == "-":
                                board[9] = player2
                                break
                            elif board[9] != "-":
                                if board[2] == "-":
                                    board[2] = player2
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        elif choice == '4':
            if board[38] == "-":
                board[38] = player2
                break
            elif board[38] != "-":
                if board[31] == "-":
                    board[31] = player2
                    break
                elif board[31] != "-":
                    if board[24] == "-":
                        board[24] = player2
                        break
                    elif board[24] != "-":
                        if board[17] == "-":
                            board[17] = player2
                            break
                        elif board[17] != "-":
                            if board[10] == "-":
                                board[10] = player2
                                break
                            elif board[10] != "-":
                                if board[3] == "-":
                                    board[3] = player2
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        elif choice == '5':
            if board[39] == "-":
                board[39] = player2
                break
            elif board[39] != "-":
                if board[32] == "-":
                    board[32] = player2
                    break
                elif board[32] != "-":
                    if board[25] == "-":
                        board[25] = player2
                        break
                    elif board[25] != "-":
                        if board[18] == "-":
                            board[18] = player2
                            break
                        elif board[18] != "-":
                            if board[11] == "-":
                                board[11] = player2
                                break
                            elif board[11] != "-":
                                if board[4] == "-":
                                    board[4] = player2
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        elif choice == '6':
            if board[40] == "-":
                board[40] = player2
                break
            elif board[40] != "-":
                if board[33] == "-":
                    board[33] = player2
                    break
                elif board[33] != "-":
                    if board[26] == "-":
                        board[26] = player2
                        break
                    elif board[26] != "-":
                        if board[19] == "-":
                            board[19] = player2
                            break
                        elif board[19] != "-":
                            if board[12] == "-":
                                board[12] = player2
                                break
                            elif board[12] != "-":
                                if board[5] == "-":
                                    board[5] = player2
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        elif choice == '7':
            if board[41] == "-":
                board[41] = player2
                break
            elif board[41] != "-":
                if board[34] == "-":
                    board[34] = player2
                    break
                elif board[34] != "-":
                    if board[27] == "-":
                        board[27] = player2
                        break
                    elif board[27] != "-":
                        if board[20] == "-":
                            board[20] = player2
                            break
                        elif board[20] != "-":
                            if board[13] == "-":
                                board[13] = player2
                                break
                            elif board[13] != "-":
                                if board[6] == "-":
                                    board[6] = player2
                                    break
                                else:
                                    print("This column is already full! Try another input.")
        else:
            print("Invalid Input: Please try again!")

def winner(board, player):
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True
    for row in range(3):
        for col in range(7):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True
    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][col - 2] == player and board[row + 3][col - 3] == player:
                return True
    return False

def convert_to_2d(board):
    return [board[i:i+7] for i in range(0, len(board), 7)]


while True:
    print_board(board)
    player1_input()
    print_board(board)
    board_2d = convert_to_2d(board)
    if winner(board_2d, player1):
        print("Player One Wins! Congratulations!")
        quit()
    elif winner(board_2d, player2):
        print("Player Two Wins! Congratulations!")
        quit()
    else:
        pass
    player2_input()
    print_board(board)
    board_2d = convert_to_2d(board)
    if winner(board_2d, player1):
        print("Player One Wins! Congratulations!")
        quit()
    elif winner(board_2d, player2):
        print("Player Two Wins! Congratulations!")
        quit()
    else:
        pass

    