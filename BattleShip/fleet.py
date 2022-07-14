from calendar import c
from re import template
from wsgiref.validate import validator
from ship import Ship

class Fleet: 
    def __init__(self):
        self.ships_list = [Ship(5, 'Carrier'), Ship(4, 'Battleship'), Ship(3, 'Cruiser'), Ship(3, 'submarine'), Ship(2, 'Destoyer')]
        self.ship_positions = []
        self.row_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    def vertical_or_horizontal(self, ship):
        user_input = input(f'\nDo you want your {ship.name} to be (1)vertically oriented, or (2)horizontally oriented?: \n')
        while user_input.isnumeric() == False or int(user_input) < 1 or int(user_input) > 2:
            print("invalid entry")
            user_input = input('\nDo you want your ship to be (1)vertically oriented, or (2)horizontally oriented?: \n')
        is_vertical = (True, False)
        return is_vertical[int(user_input) -1]


    
    def vertical_coordinate(self, ship):
        letter_start = input(f'Choose a letter between a-{self.row_letters[len(self.row_letters) - ship.hitpoints]} this will be the point of {ship.name} nearest the top of the game board: ')
        while letter_start.isalpha() == False or len(letter_start) > 1:
            print('Invalid entry. Must be a single letter.')
            letter_start = input(f'Choose a letter between a-{self.row_letters[len(self.row_letters) - ship.hitpoints]} this will be the point of {ship.name} nearest the top of the game board: ')
        while self.row_letters.index(letter_start) + ship.hitpoints > 10 or self.row_letters.index(letter_start) + ship.hitpoints < 1:
                print('Invalid Entry. Your entire ship must fit on the gameboard.')
                letter_start = input(f'Choose a letter between a-{self.row_letters[len(self.row_letters) - ship.hitpoints]} this will be the point of {ship.name} nearest the top of the game board: ')
        column_num = input(f'Choose a number between 1-10 this is the column where your {ship.name} will be positioned: ' )
        while column_num.isnumeric() == False or int(column_num) > 10 or int(column_num) < 1:
            print('Invalid entry. Must be a number between 1-10.')
            column_num = input(f'Choose a number between 1-10 this is the column where your {ship.name} will be positioned: ' )
        coordinate = [letter_start, column_num]                 
        return coordinate

    def vertical_position(self, ship, coordinate):
        temp_list = []
        for index in range((self.row_letters.index(coordinate[0]) + 1), (ship.hitpoints + self.row_letters.index(coordinate[0]))): 
            if any(filter(lambda c: ((self.row_letters[index] + str(coordinate[1])) == c), self.ship_positions)):
                print(f'Your {ship.name} cannot occupy the same space as another ship')
                self.vertical_coordinate(ship)
            else:
                temp_list.append(self.row_letters[index] + str(index))
        ship.position.extend(temp_list)
        self.ship_positions.extend(temp_list)
        temp_list = []

    def horizontal_coordinate(self, ship):
            row_letter = input(f'choose a letter between a-j this is the row where your {ship.name} will be positioned: ')
            while row_letter.isalpha() == False or len(row_letter) > 1:
                print('Invalid entry. Must be a single letter.')
                row_letter = input(f'choose a letter between a-j this is the row where your {ship.name} will be positioned: ')
            number_start = input(f'Choose a number between 1-{11 - ship.hitpoints} this will be the left-most point of your {ship.name}: ')
            while number_start.isnumeric() == False or int(number_start) + ship.hitpoints > 11:
                print('Invalid Entry. Your entire ship must fit on the gameboard.')
                number_start = int(input(f'Choose a number between 1-{11 - ship.hitpoints} this will be the left-most point of your {ship.name}: ')) 
            coordinate = [row_letter, number_start]
            return coordinate
    
    def horizontal_position(self, ship, coordinate):
            temp_list = []
            for index in range(int(coordinate[1]), (ship.hitpoints + (int(coordinate[1]) - 1))): 
                if any(filter(lambda c: coordinate[0] + str(index) == c, self.ship_positions)):
                    print(f'Your {ship.name} cannot occupy the same space as another ship')
                    self.vertical_coordinate(ship)
                else:
                    temp_list.append(coordinate[0] + str(index))
            ship.position.extend(temp_list)
            self.ship_positions.extend(temp_list)
            temp_list = []

            





    def choose_positions(self):
        for ship in self.ships_list:
            if self.vertical_or_horizontal(ship):
                self.vertical_position(ship, self.vertical_coordinate(ship))
            else: 
                self.horizontal_position(ship, self.horizontal_coordinate(ship))

