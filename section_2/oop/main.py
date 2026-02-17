from enemy import Enemy

enemy = Enemy()

enemy.type_of_enemy = 'Zombie'

print(f"{enemy.type_of_enemy} has {enemy.health_points} health points and can do attacks of {enemy.attack_damage}")