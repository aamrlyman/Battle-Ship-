from ship import Ship

class Player: 
    def __init__(self) -> None:
        self.fleet = [Ship(5, 'Carrier'), Ship(4, 'Battleship'), Ship(3, 'Cruiser'), Ship(3, 'submarine'), Ship(2, 'Destoyer')]
        self.attack_log = []
        self.self.ship_positions = [self.fleet[0].position, self.fleet[1].position, self.fleet[2].position, self.fleet[3].position, self.fleet[4].position] 
    

    

    def attack(self, opponent):
        print(self.attack_log)
        attack_coordinate = input('Type a letter and number in this format: c5, for where you will attack: ')
        for ship in opponent.fleet:
            for coordinate in ship.position:
                if attack_coordinate == coordinate: 
                    ship.hitpoints -=1
                    self.attack_log.append(attack_coordinate)
                    print(f"You hit your oppoent's {ship.name}. Their {ship.name} has {ship.hitpoints} left.")
                else:
                    print('You attack was a miss.')

