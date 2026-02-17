class Enemy:

    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1
    
    def talk(self): # Using a function or variable inside the call requires self as it is referring to itself
        print(f'I am an {self.type_of_enemy}. Be prepared to fight.')

    def walk_forward(self):
        print(f'{self.type_of_enemy} moves closer')
    
    def attack(self):
        print(f'{self.type_of_enemy} attacks for {self.attack_damage} damage')