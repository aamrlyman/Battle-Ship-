from ship import Ship

class Fleet: 
    def __init__(self):
        self.ships_list = [Ship(5, 'Carrier'), Ship(4, 'Battleship'), Ship(3, 'Cruiser'), Ship(3, 'submarine'), Ship(2, 'Destoyer')]
        self.ship_positions = []
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    def vertical_or_horizontal(self):
        user_input = input('\nDo you want your ship to be (1)vertically oriented, or (2)horizontally oriented?: \n')
        while user_input.isnumeric() == False or int(user_input) < 1 or int(user_input) > 2:
            print("invalid entry")
            user_input = input('\nDo you want your ship to be (1)vertically oriented, or (2)horizontally oriented?: \n')
        is_vertical = (True, False)
        return is_vertical[int(user_input)]



    def vertical_coordinate(self):
        letter_start = input(f'Choose a letter between a-{self.letters[len(self.letters) - self.hitpoints]} this will be the point of {self.name} nearest the top of the game board: ')
        column_num = input(f'Choose a number between 1-10 this is the column where your {self.name} will be positioned: ' )
        while self.letters.index(letter_start) + self.hitpoints > 10 or self.letters.index(letter_start) + self.hitpoints < 1:
                print('Invalid Entry. Your entire ship must fit on the gameboard.')
                letter_start = input(f'Choose a letter between a-{self.letters[len(self.letters) - self.hitpoints]} this will be the point of {self.name} nearest the top of the game board: ')
        coordinate = [letter_start, column_num]                 
        return coordinate

    def vertical_position(self, coordinate):
        
        for index in range(self.letters.index(coordinate[0]), (self.hitpoints + self.letters.index(coordinate[0]))): 
            if any(filter(lambda c: ((self.letters[index] + str(coordinate[1])) == c), self.ship_positions)):
                print(f'Your {self.name} cannot occupy the same space as another ship')
                self.vertical_coordinate()
            else:
                self.position.append(self.letters[index] + coordinate[1])
            


            row_letter = input(f'choose a letter between a-j this is the row where your {self.name} will be positioned: ')
            number_start = int(input(f'Choose a number between 1-{11 - self.hitpoints} this will be the left-most point of your {self.name}: '))
            while number_start + self.hitpoints > 11:
                print('Invalid Entry. Your entire ship must fit on the gameboard.')
                number_start = input('Choose a number betwen 1-10 this will be the high point of the ship: ')                 
                position = []
            for index in range(number_start, (self.hitpoints + number_start)): 
                position.append(row_letter + str(index))
                self.ship_positions.append(row_letter + str(index))
            self.position = position
            return self.position
            
    def choose_position(self):
        print('')
        print_board()
        self.is_vertical = True if int(input(f'Will your {self.name} hitpoint ship be (1)vertical or (2)horizontal?: ')) == 1 else False
        if self.is_vertical:
            pass