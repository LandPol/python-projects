from random import choice

def printBoard(board):
    print(f"\n{board[0]} | {board[1]} | {board[2]}\
          \n---------\n{board[3]} | {board[4]} | {board[5]}\
          \n---------\n{board[6]} | {board[7]} | {board[8]}")
    
def playerMove(symbol, idx, board):
    if board[idx - 1] == ' ':
        board[idx - 1] = symbol
        return board
    else:
        print("This place was already choosen.")

def getAvailableMoves(board):
    empty = [i for i, value in enumerate(board) if value == ' ']
    return empty

def getWinner(board):
    w_comb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in w_comb:
        if board[i[0]] == board[i[1]] == board[i[2]] != ' ':
            return board[i[0]]
    if ' ' not in board:
        return "DRAW"
    return None
            
def checkWinner(board, active_player):
    winner = getWinner(board)
    if winner is not None:
        printBoard(board)
        if winner == "DRAW":
            print("\nThe game is end. Draw.")
        else:
            print(f"\nPlayer {active_player} wins!")
    return winner

def aiMoveEasy(board, ai_symbol, player_symbol):
    move = choice(getAvailableMoves(board))
    board[move] = ai_symbol
    return board

def aiMoveMedium(board, ai_symbol, player_symbol):
    for move in getAvailableMoves(board):
        board_copy = board.copy()
        board_copy[move] = player_symbol
        if checkWinner(board_copy, player_symbol) == player_symbol:
            board[move] = ai_symbol
            return board
    move = choice(getAvailableMoves(board))
    board[move] = ai_symbol
    return board

def minimax(board, depth, is_maximizing, ai_symbol, player_symbol):
    winner = getWinner(board) or getWinner(board)
    if winner == ai_symbol:
        return 1
    elif winner == player_symbol:
        return -1
    elif winner == "DRAW":
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for move in getAvailableMoves(board):
            board[move] = ai_symbol
            score = minimax(board, depth + 1, False, ai_symbol, player_symbol)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in getAvailableMoves(board):
            board[move] = player_symbol
            score = minimax(board, depth + 1, True, ai_symbol, player_symbol)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score
    
def aiMoveHard(board, ai_symbol, player_symbol):
    best_score = -float('inf')
    best_move = None
    for move in getAvailableMoves(board):
        board[move] = ai_symbol
        score = minimax(board, 0, False, ai_symbol, player_symbol)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = ai_symbol
    return board

def game():
    m = input("Choose mode: 1) Player vs Player, 2) Player vs AI: ")
    if m == "2":
        diff = input("Choose AI difficulty: 1) Easy, 2) Medium, 3) Hard: ")
    board = [' ' for i in range(9)]
    active_player = 0
    players = ['O', 'X']

    while True:
        print("\n--- Tic Tac Toe ---\n")
        printBoard(board)
        if active_player == 1 and m == "2":
            if diff == "1":
                board = aiMoveEasy(board, players[active_player], players[0])
            elif diff == "2":
                board = aiMoveMedium(board, players[active_player], players[0])
            else:
                board = aiMoveHard(board, players[active_player], players[0])
            if checkWinner(board, players[active_player]) == players[active_player]:
                break
            active_player = 1 - active_player
        else:
            while True:
                try:
                    p = int(input(f"\nPlayer {active_player + 1} turn. Choose your action: "))
                    break
                except ValueError:
                    print("ERROR: Invalid value.")
            if 1 <= p <= 9:
                    if playerMove(players[active_player], p, board):
                        if checkWinner(board, players[active_player]) is not None:
                            break
                        active_player = 1 - active_player

            elif p == 0:
                print("\nBye")
                break
            else: 
                print("Invalid place choosen.")
            


game()