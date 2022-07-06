from ship import Ship

class Player: 
    def __init__(self) -> None:
        self.carrier = Ship(5, 'Carrier')
        self.battleship = Ship(4, 'Battleship') 
        self.cruiser = Ship(3, 'Cruiser')
        self.submarine =  Ship(3, 'submarine') 
        self.destoryer = Ship(2, 'Destoyer')
        self.fleet = [self.carrier, self.battleship, self.cruiser, self.submarine, self.destoryer]
        self.attack_log = []