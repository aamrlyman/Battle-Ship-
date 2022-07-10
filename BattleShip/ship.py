from practicePrint import print_board
        #find a method that compares each one element to the items on a list 
        #find a way to print ship positions on a grid and an attacks log in the console
        #find a way to differentiate hits from misses in log 


class Ship: 
    def __init__(self, health, name) -> None:
        self.hitpoints = int(health)
        self.is_vertical = True
        self.name = name
        self.position = None
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    def vertical_coordinate(self):
        letter_start = input(f'Choose a letter between a-{self.letters[len(self.letters) - self.hitpoints]} this will be the point of {self.name} nearest the top of the game board: ')
        column_num = input(f'Choose a number between 1-10 this is the column where your {self.name} will be positioned: ' )
        while self.letters.index(letter_start) + self.hitpoints > 10 or self.letters.index(letter_start) + self.hitpoints < 1:
                print('Invalid Entry. Your entire ship must fit on the gameboard.')
                letter_start = input(f'Choose a letter between a-{self.letters[len(self.letters) - self.hitpoints]} this will be the point of {self.name} nearest the top of the game board: ')
        coordinate = [letter_start, column_num]                 
        return coordinate

    def vertical_position(self, coordinate):
        position = []
        occupied_tiles = []
        for index in range(self.letters.index(coordinate[0]), (self.hitpoints + self.letters.index(coordinate[0]))): 
            if any(filter(lambda c: ((self.letters[index] + str(coordinate[1])) == c), occupied_tiles)):
                print(f'Your {self.name} cannot occupy the same space as another ship')
                self.vertical_coordinate()
            else:
                position.append(self.letters[index] + coordinate[1])
                occupied_tiles.append(self.letters[index] + coordinate[1])
            self.position = position

        # else:
        #     row_letter = input(f'choose a letter between a-j this is the row where your {self.name} will be positioned: ')
        #     number_start = int(input(f'Choose a number between 1-{11 - self.hitpoints} this will be the left-most point of your {self.name}: '))
        #     while number_start + self.hitpoints > 11:
        #         print('Invalid Entry. Your entire ship must fit on the gameboard.')
        #         number_start = input('Choose a number betwen 1-10 this will be the high point of the ship: ')                 
        #         position = []
        #     for index in range(number_start, (self.hitpoints + number_start)): 
        #         position.append(row_letter + str(index))
        #         occupied_tiles.append(row_letter + str(index))
        #     self.position = position
        #     return self.position
            
    # def choose_position(self):
    #     print('')
    #     print_board()
    #     self.is_vertical = True if int(input(f'Will your {self.name} hitpoint ship be (1)vertical or (2)horizontal?: ')) == 1 else False
    #     if self.is_vertical:

