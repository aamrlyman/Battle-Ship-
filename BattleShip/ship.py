        #find a method that compares each one element to the items on a list 
        #find a way to print ship positions on a grid and an attacks log in the console
        #find a way to differentiate hits from misses in log 


class Ship: 
    def __init__(self, health, name) -> None:
        self.hitpoints = int(health)
        self.is_vertical = True
        self.name = name
        self.position = self.choose_position() 
    
    def choose_position(self):
        print('')
        self.is_vertical = True if int(input(f'Will your {self.name} hitpoint ship be (1)vertical or (2)horizontal?: ')) == 1 else False
        occupied_tiles = []
        if self.is_vertical:
            column_num = input(f'Choose a number between 1-10 this is the column where your {self.name} will be positioned: ' )
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
            letter_start = input(f'Choose a letter between a-{letters[len(letters) - self.hitpoints]} this will be the point of {self.name} nearest the top of the game board: ')
            while letters.index(letter_start) + self.hitpoints > 10:
                print('Invalid Entry. Your entire ship must fit on the gameboard.')
                letter_start = input('Choose a letter between a-j this will be the top-most point of the ship: ')                 
                position = []
            for index in range(letters.index(letter_start), (self.hitpoints + letters.index(letter_start))): 
                position.append(letters[index] + column_num)
            self.position = position
            return self.position
        else:
            row_letter = input(f'choose a letter between a-j this is the row where your {self.name} will be positioned: ')
            number_start = int(input(f'Choose a number between 1-{11 - self.hitpoints} this will be the left-most point of your {self.name}: '))
            while number_start + self.hitpoints > 11:
                print('Invalid Entry. Your entire ship must fit on the gameboard.')
                number_start = input('Choose a number betwen 1-10 this will be the high point of the ship: ')                 
                position = []
            for index in range(number_start, (self.hitpoints + number_start)): 
                position.append(row_letter + str(index))
            self.position = position
            return self.position
            
ship1 = Ship(5)
ship1.choose_position()
print(ship1.position)