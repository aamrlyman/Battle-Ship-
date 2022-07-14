from practicePrint import print_board


        # find a method that compares each one element to the items on a list 
        # find a way to print ship positions on a grid and an attacks log in the console
        # find a way to differentiate hits from misses in log 


class Ship: 
    def __init__(self, health, name) -> None:
        self.name = name
        self.hitpoints = int(health)
        self.position = []
        
   
