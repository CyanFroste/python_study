hero = {
    "name": "Thane",
    "health": 100,
    "atk": 10,
}

enemy = {
    "name": "Goblin",
    "health": 100,
    "atk": 5,
}


def attack(attacker, defender):
    defender["health"] -= attacker["atk"]


def is_alive(character):
    return character["health"] > 0


def playable(a, character1, character2):
    return a != "Q" and is_alive(character1) and is_alive(character2)


action = input("What do you want to do? (attack: A/quit: Q) ")

turn = 1

while playable(action, enemy, hero):  # we play until the user quits

    print('Turn', turn)

    # play one turn
    target = input("Who do you want to attack? (enemy: E/hero: H) ")
    if target == "E":
        attack(hero, enemy)
    else:
        attack(enemy, hero)

    # after a turn
    turn += 1
    print(f"{hero['name']}'s health: {hero['health']}")
    print(f"{enemy['name']}'s health: {enemy['health']}")

    action = input("What do you want to do? (attack: A/quit: Q) ")
