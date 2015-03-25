import random

attackRoll = 0
strMod = 3
dexMod = 1
melee = 0
size = 1
ranged = 1
dieface = 6
die = 2
i = 0
rollOne = 0
rollTwo = 0

if melee and ranged > 1:
    attack = random.randint(1, 2)
    if attack == 1:
        roll = random.randint(1, 20)
        attackRoll = (roll + strMod + size)
        if roll == 1:
            return False

        elif roll <= 19:
            while i < die:
                rollOne += random.randint(1, dieface)
                i += 1

            damage = rollOne + melee
            return damage

        elif roll == 20:
            while i < die:
                rollOne += random.randint(1, dieface)
                i += 1

            i = 0
            damage = rollOne + melee
            while i < die:
                rollTwo += random.randint(1, dieface)
                i += 1

            damageCrit = rollTwo + melee
            return damage, damageCrit

    elif attack == 2:
        roll = random.randint(1, 20)
        attackRoll = (roll + dexMod + size)
        if roll == 1:
            return False

        elif roll <= 19:
            while i < die:
                rollOne += random.randint(1, dieface)
                i += 1

            damage = rollOne + ranged
            return damage

        elif roll == 20:
            while i < die:
                rollOne += random.randint(1, dieface)
                i += 1

            i = 0
            damage = rollOne + ranged
            while i < die:
                rollTwo += random.randint(1, dieface)
                i += 1

            damageCrit = rollTwo + ranged
            return damage, damageCrit

if ranged >= 1:
    roll = random.randint(1, 20)
    attackRoll = (roll + dexMod + size)
    if roll == 1:
        return False

    elif roll <= 19:
        while i < die:
            rollOne += random.randint(1, dieface)
            i += 1

        damage = rollOne + ranged
        return damage

    elif roll == 20:
        while i < die:
            rollOne += random.randint(1, dieface)
            i += 1

        i = 0
        damage = rollOne + ranged
        while i < die:
            rollTwo += random.randint(1, dieface)
            i += 1

        damageCrit = rollTwo + ranged
        return damage, damageCrit

elif melee >= 1:
    roll = random.randint(1, 20)
    attackRoll = (roll + strMod + size)
    if roll == 1:
        return False

    elif roll <= 19:
        while i < die:
            rollOne += random.randint(1, dieface)
            i += 1

        damage = rollOne + melee
        return damage

    elif roll == 20:
        while i < die:
            rollOne += random.randint(1, dieface)
            i += 1

        i = 0
        damage = rollOne + melee
        while i < die:
            rollTwo += random.randint(1, dieface)
            i += 1

        damageCrit = rollTwo + melee
        return damage, damageCrit
