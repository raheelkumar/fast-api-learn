class Enemy:

    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
    
    def talk(self): # Using a function or variable inside the call requires self as it is referring to itself
        print(f'I am an {self.type_of_enemy}. Be prepared to fight.')

    def walk_forward(self):
        print(f'{self.type_of_enemy} moves closer')
    
    def attack(self):
        print(f'{self.type_of_enemy} attacks for {self.attack_damage} damage')