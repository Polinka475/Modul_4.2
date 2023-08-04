import random

class Tank:
    def __init__(self, model, armor, min_damage, max_damage, health):
        self.model = model
        self.armor = armor
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.health = health

    def print_info(self):
        print(f'{self.model} имеет броню {self.armor} мм при {self.health} здоровье и средний урон {(self.min_damage + self.max_damage)//2}')

    def health_down(self, enemy_damage):
        self.health -= (enemy_damage - (self.armor // 10))
        if self.health < 0:
            self.health = 0

    def shot(self, enemy):
        enemy.health_down(random.randint(self.min_damage, self.max_damage))
        print(f'\n{self.model}:')
        if enemy.health > 0:
            print(f'Точно в цель, у противника {self.model} осталось {self.health} здоровья')
        else:
            print(f'Экипаж танка {self.model} уничтожен!')

tank_1 = Tank('т-39', 90, 20, 30, 100)
tank_2 = Tank('Tiger', 100, 10, 40, 100)

tank_1.print_info()
tank_2.print_info()

tank_2.shot(tank_1)
