

board = [' ' for _ in range(9)]

def choose_symbol():
    while True:
        player_choice = input('Do you want to be X? (y/n): ')
        if player_choice.lower() == 'y':
            player = 'X'
            computer = 'O'
            return player, computer
        elif player_choice.lower() == 'n':
            player = 'O'
            computer = 'X'
            return player, computer
        else:
            print("Invalid input. Please enter 'y' for X or 'n' for O.")


    
def print_board():
    print('--------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('--------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('--------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('--------------')

print_board()

def is_empty():
    return ' ' in board

def is_full():
    return not is_empty()

def check_winner_in_row(symbol):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] == symbol:
            return board[i]
    
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] == symbol:
            return board[i]
        
    if board[0] == board[4] == board[8] == symbol or board[2] == board[4] == board[6] == symbol:
        return True
    
    return False

def player_move(player):
    while True:
        move = input('Enter your move (0-8): ')
        move = int(move)
        if board[move] == ' ':
            board[move] = player
            print_board()
            if check_winner_in_row(player):
                print('You win!')
                return
            elif is_full():
                print('Draw!')
                return
            else:
                return
        else:
            print('Invalid move. Try again')

def computer_move(computer,player):
    for i in range(9):
        if board[i] == ' ':
            board[i] = computer
            if check_winner_in_row(computer):
                print_board()
                print('Computer wins!')
                return
            board[i] = ' '

    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            if check_winner_in_row(player):
                board[i] = computer
                print_board()
                return
            board[i] = ' '

    if board[4] == ' ':
        board[4] = computer
        print_board()
        return

    for i in [0, 2, 6, 8]:
        if board[i] == ' ':
            board[i] = computer
            print_board()
            return

    for i in [1, 3, 5, 7]:
        if board[i] == ' ':
            board[i] = computer
            print_board()
            return

def main():
    print("Welcome to Tic-Tac-Toe!")
    player, computer = choose_symbol()
    print_board()
    turn = 'player'

    while True:
        if turn == 'player':
            player_move(player)
            if check_winner_in_row(player) or is_full():
                break
            turn = 'computer'
        elif turn == 'computer':
            computer_move(computer,player)
            if check_winner_in_row(computer) or is_full():
                break
            turn = 'player'

    print("Game Over.")

if __name__ == "__main__":
    main()