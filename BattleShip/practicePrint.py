Alphabet = ['a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j']
coordinates = ['a1', 'e6','a4']

def show_top_of_board():
        top_of_board = ''
        for num in range(0, 11):
            num = str(num)
            top_of_board += num + "   "
        print (top_of_board)


def rest_game_board():
    row = ''
    for letter in Alphabet:
        row += letter.upper() + '   '
        for num in range(0,10):
            if any(filter((lambda x: x[0] == letter and (int(x[1]) -1) == num), coordinates)):
                row += letter + str(num + 1) + '  ' 
            else:
                row += '__' + '  '
        print(row)
        row = ''
    print('')

def print_board():
    show_top_of_board()
    rest_game_board()


print_board()