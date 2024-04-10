import random


class Character:
    def __init__(self, name, hp, damage, bron):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.evasion = bron

    def attack(self, target):
        attack_damage = random.randint(1, self.damage)
        evasion_chance = random.randint(1, 10)
        if evasion_chance > target.evasion:
            print(f"{self.name} атакует {target.name} и наносит {attack_damage} урона.")
            target.hp -= attack_damage
        else:
            print(f"{self.name} атакует {target.name}, но {target.name} уклоняется от атаки!")

class Player(Character):
    def __init__(self, name, hp, damage, evasion):
        super().__init__(name, hp, damage, evasion)

class Enemy(Character):
    def __init__(self, name, hp, damage, evasion):
        super().__init__(name, hp, damage, evasion)

player = Player("Игрок", 40, 8, 3)

def generate_random_enemy():
    enemy_names = ["Leshy", "Vampir", "Zomby", "Sprut", "Sclet", "Leshy1", "Vampir1", "Zomby1", "Sprut1", "Sclet1"]
    enemy_name = random.choice(enemy_names)
    enemy_hp = random.randint(5, 10)
    enemy_damage = random.randint(1, 4)
    enemy_evasion = random.randint(1, 5)
    return Enemy(enemy_name, enemy_hp, enemy_damage, enemy_evasion)

def battle(player, enemy):

    print(f"{player.name} встречает {enemy.name}!")
    while player.hp > 0 and enemy.hp > 0:
        player.attack(enemy)
        if enemy.hp <= 0:
            print(f"{player.name} побеждает!")
            break
        enemy.attack(player)
        if player.hp <= 0:
            print(f"{enemy.name} побеждает!")
            break
class Menu:
    def __init__(self):
        player.name = input("Введите ваше имя - ")

    def menu(self):
        print(f'Добро пожаловать в игру, {player.name}.')
        choice = int(input('''Что вы хотите сделать?
        1 - Начать новую игру.
        2 - Выйти\n'''))
        if choice == 1:
            difficulty = int(input('''Выберите уровень сложности.
        1 - Легкий
        2 - Средний
        3 - Сложный\n'''))
            return difficulty
        if choice == 2:
            pass


menu = Menu()
menu.menu()

print(f"Добро пожаловать, {player.name}!")
while player.hp > 0:
    print(f"Текущее здоровье: {player.hp}")
    choice = input("1. Идти вперед\n2. Выход из игры\nВыберите действие: ")

    if choice == "1":
        random_enemy = generate_random_enemy()
        battle(player, random_enemy)
    elif choice == "2":
        print("До свидания! Спасибо за игру.")
        break
    else:
        print("Некорректный выбор.")

if player.hp <= 0:
    print("Игра окончена. Вы проиграли.")