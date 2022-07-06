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
    
    def attack(self):
        print(self.attack_log)
        attack_coordinate = input('Type a letter and number in this format (c5) for where you will attack: ')
        for ship in self.fleet:
            for coordinate in ship.position:
                if attack_coordinate == coordinate: 
                    ship.hitpoints -=1
                    self.attack_log.append(attack_coordinate)
                    print(f"You hit your oppoent's {ship.name}. Their {ship.name} has {ship.hitpoints} left.")
                else:
                    print('You attack was a miss.')