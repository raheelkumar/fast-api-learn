from zombie import Zombie
from ogre import Ogre

zombie = Zombie(10, 1)

print(f"{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do attacks of {zombie.attack_damage}")
zombie.talk()
zombie.spread_disease()

ogre = Ogre(20,3)

print(f"{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do attacks of {ogre.attack_damage}")
ogre.talk()