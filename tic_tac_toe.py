import math

def AIagent_move(board):
    best_score = -math.inf
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                score = MINI(board, 0, False, -math.inf, math.inf)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

def MINI(board, depth, is_maximizing, alpha, beta):
    if Win_Result(board, 'O'):
        return 10 - depth
    elif Win_Result(board, 'X'):
        return depth - 10
    elif Draw_scenario(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = MINI(board, depth + 1, False, alpha, beta)
                    board[row][col] = ' '
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = MINI(board, depth + 1, True, alpha, beta)
                    board[row][col] = ' '
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def Win_Result(board, player):
 
    for row in range(3):
        if all([board[row][col] == player for col in range(3)]):
            return True

    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

   
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

def Draw_scenario(board):
    return all([board[row][col] != ' ' for row in range(3) for col in range(3)])
