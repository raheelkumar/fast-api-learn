from enemy import Enemy
from zombie import Zombie
from ogre import Ogre
from hero import Hero
from weapon import Weapon

zombie = Zombie(10, 1)
ogre = Ogre(20,3)
hero = Hero(10, 1)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equipWeapon()

def hero_battle(hero: Hero, enemy: Enemy):
    
    while hero.health_points > 0 and enemy.health_points > 0:
        print('----------------------------------')
        enemy.special_attack()
        print(f'Hero: {hero.health_points} HP left')
        print(f'{enemy.get_type_of_enemy()}: {enemy.health_points} HP left')
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

        if hero.health_points > 0:
            print(f'Hero wins!')
        else:
            print(f'{enemy.get_type_of_enemy()} wins!')

hero_battle(hero, zombie)