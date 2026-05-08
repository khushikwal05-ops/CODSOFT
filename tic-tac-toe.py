import math
import time

board = [' ' for _ in range(9)] # 3x3 board

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def is_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6] # diagonals
    ]
    for condition in win_conditions:
        if brd[condition[0]] == brd[condition[1]] == brd[condition[2]] == player:
            return True
    return False

def is_board_full(brd):
    return ' ' not in brd

def get_available_moves(brd):
    return [i for i, spot in enumerate(brd) if spot == ' ']

def minimax(brd, depth, is_maximizing, alpha, beta):
    """
    Minimax algorithm with Alpha-Beta Pruning
    AI = 'O' is maximizing player, Human = 'X' is minimizing player
    """
    if is_winner(brd, 'O'):
        return 10 - depth
    if is_winner(brd, 'X'):
        return depth - 10
    if is_board_full(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(brd):
            brd[move] = 'O'
            score = minimax(brd, depth + 1, False, alpha, beta)
            brd[move] = ' '
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha: # Alpha-Beta Pruning
                break
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(brd):
            brd[move] = 'X'
            score = minimax(brd, depth + 1, True, alpha, beta)
            brd[move] = ' '
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha: # Alpha-Beta Pruning
                break
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in get_available_moves(board):
        board[i] = 'O'
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    return move

def player_move():
    while True:
        try:
            move = int(input('Enter your move (1-9): ')) - 1
            if move >= 0 and move <= 8 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print('Invalid move. That spot is taken or out of range.')
        except ValueError:
            print('Please enter a number between 1 and 9.')

def main():
    print("=== CODSOFT Task 2: Tic-Tac-Toe AI ===")
    print("You are 'X' | AI is 'O'")
    print("Positions: 1|2|3 4|5|6 7|8|9\n")

    print_board()

    while True:
        # Human turn
        player_move()
        print("\nAfter your move:")
        print_board()

        if is_winner(board, 'X'):
            print("\n🎉 You win! Wait... that's impossible vs Minimax!")
            break
        if is_board_full(board):
            print("\n🤝 It's a draw!")
            break

        print("\nAI is thinking...")
        time.sleep(0.5) # Dramatic effect
        ai_move = best_move()
        board[ai_move] = 'O'
        print(f"AI chose position {ai_move + 1}")
        print("\nAfter AI move:")
        print_board()

        if is_winner(board, 'O'):
            print("\n🤖 AI wins! Minimax is unbeatable.")
            break
        if is_board_full(board):
            print("\n🤝 It's a draw!")
            break

if __name__ == "__main__":
    main()