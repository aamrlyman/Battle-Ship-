Alphabet = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J']

def show_top_of_board():
        top_of_board = ''
        for num in range(0, 11):
            num = str(num)
            top_of_board += num + "   "
        print (top_of_board)

def rest_game_board():
    row = ''
    for letter in Alphabet:
        row += letter + '   '
        for num in range(0,10):
            num = str(num)
            row += '__' + '  '
        print(row)
        row = ''

def print_board():
    show_top_of_board()
    rest_game_board()
