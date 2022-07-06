


class Ship: 
    def __init__(self, health) -> None:
        self.hitpoints = int(health)
        self.is_vertical = True
        self.position = {}
    
    def choose_position(self):
        self.is_vertical = True if int(input(f'Will your {self.hitpoints} hitpoint ship be (1)vertical or (2)horizontal?: ')) == 1 else False
        if self.is_vertical:
            new_key = input(f'Choose a number between 1-10 this is the column where your {self.hitpoints} hitpoint ship will be positioned: ' )
            letter_start = input('Choose a letter between a-j this will be the high point of the ship: ')
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
            while letters.index(letter_start) + self.hitpoints > 10:
                print('Invalid Entry. Your entire ship must fit on the gameboard.')
                letter_start = input('Choose a letter between a-j this will be the top-most point of the ship: ')                
            new_value = [] 
            for index in range(letters.index(letter_start), (self.hitpoints + letters.index(letter_start))): 
                new_value.append(letters[index])
            self.position[new_key] = new_value
        else:
            new_key = input(f'choose a letter between a-j this is the row where your {self.hitpoints} hitpoint ship will be positioned: ')
            number_start = int(input('Choose a number between 1-10 this will be the left-most point of the ship: '))
            while number_start + self.hitpoints > 10:
                print('Invalid Entry. Your entire ship must fit on the gameboard.')
                number_start = input('Choose a number betwen 1-10 this will be the high point of the ship: ')                
            new_value = [] 
            for index in range(number_start, (self.hitpoints + number_start)): 
                new_value.append(index)
            self.position[new_key] = new_value

ship1 = Ship(5)
ship1.choose_position()
print(ship1.position)