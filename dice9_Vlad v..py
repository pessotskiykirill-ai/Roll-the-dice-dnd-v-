from random import randint
print("Добро пожаловать солага, здесь ты можешь считать дайсы по быстренькому ::D")
dice_dict = dict()

def dice_rd(n):
    all_list_damage = list()
    all_damage = 0
    sred_damage = 0
    d_n = 4

    if n == 0: # Первый варинат функции, когда набираются первый раз значения
        for i in range(1,7):
            list_damage = []
            if d_n <= 12: # Условия для d4,6,8,10,12
                dice = int(input(f"Количество d{d_n}: "))
                all_damage += dice_ran_calcul(d_n, dice, list_damage, all_list_damage)
                sred_damage += sred_damage_calcul(d_n, dice)
                dice_dict[d_n] = dice
                d_n += 2

        mod = int(input("Модификатор урона: "))
        all_list_damage.append("+ "+str(mod))
        all_damage += mod
        sred_damage += mod
        dice_dict[21] = mod


    else: # Второй варинт функции, для переброса кубов
        for i,j in dice_dict.items():
            list_damage = []
            if i != 21:
                all_damage += dice_ran_calcul(i, j, list_damage, all_list_damage)
                sred_damage += sred_damage_calcul(i, j)


            else:
                all_damage += j
                sred_damage += j
                all_list_damage.append("+ "+str(j))


    print("\n----Вывод----")
    d_n = 4
    for i in range(len(all_list_damage)):
        if i <= 4: # Специально для d4,6,8,10,12
            if len(all_list_damage[i]) == 0: # Если для дайс не кидали, то он не попадется в вкладку вывод
                d_n += 2
                continue
            else:
                print(f"Броски d{d_n}: {all_list_damage[i]}")
            d_n += 2

        else: # Специально для Модфикатора урона
            print(f"Модификатор урона: {all_list_damage[i]}")


    print(f"\nОбщий урон: {all_damage}\nСредний урон: {sred_damage}\n")

def dice20(n, bonus, floor, advantage, crit_suc, crit_fail):
    results = []
    success = 0
    crit_success = 0
    failure = 0
    crit_failure = 0
    for i in range(n):
        roll1 = randint(1, 20)
        roll2 = randint(1, 20)
        if advantage == 1:
            if roll1 > roll2:
                roll = roll1
            else:
                roll = roll2
        elif advantage == -1:
            if roll1 > roll2:
                roll = roll2
            else:
                roll = roll1
        else:
            roll = randint(1, 20)

        if roll >= crit_suc:
            stat = "Крит"
            crit_success += 1
        elif roll <= crit_fail:
            stat = "Крит провал"
            crit_failure += 1
        else:
            stat = (roll + bonus)
            if stat >= floor:
                success += 1
            else:
                failure += 1
        results.append(stat)
    print(f"Результаты с бонусами: {results}")
    print(f"Успешные броски:{success}")
    print(f"Критически успешные броски:{crit_success}")
    print(f"Провальные броски:{failure}")
    print(f"Критически провальные броски:{crit_failure}")

def dice_ran_calcul(d_n, dice, list_damage, all_list_damage):
from random import randint
print("Добро пожаловать солага, здесь ты можешь считать урон по быстренькому ::D")
dice_dict = dict()

def dice_rd(n): # Броски дайсов на урон
    all_list_damage = list()

from random import randint
print("Добро пожаловать солага, здесь ты можешь считать дайсы по быстренькому ::D")
dice_dict = dict()

def dice_rd(n):
    all_list_damage = list()
    all_damage = 0
    sred_damage = 0
    d_n = 4

    if n == 0: # Первый варинат функции, когда набираются первый раз значения
        for i in range(1,7):
            list_damage = []
            if d_n <= 12: # Условия для d4,6,8,10,12
                dice = int(input(f"Количество d{d_n}: "))
                all_damage += dice_ran_calcul(d_n, dice, list_damage, all_list_damage)
                sred_damage += sred_damage_calcul(d_n, dice)
                dice_dict[d_n] = dice
                d_n += 2

        mod = int(input("Модификатор урона: "))
        all_list_damage.append("+ "+str(mod))
        all_damage += mod
        sred_damage += mod
        dice_dict[21] = mod


    else: # Второй варинт функции, для переброса кубов
        for i,j in dice_dict.items():
            list_damage = []
            if i != 21:
                all_damage += dice_ran_calcul(i, j, list_damage, all_list_damage)
                sred_damage += sred_damage_calcul(i, j)


            else:
                all_damage += j
                sred_damage += j
                all_list_damage.append("+ "+str(j))


    print("\n----Вывод----")
    d_n = 4
    for i in range(len(all_list_damage)):
        if i <= 4: # Специально для d4,6,8,10,12
            if len(all_list_damage[i]) == 0: # Если для дайс не кидали, то он не попадется в вкладку вывод
                d_n += 2
                continue
            else:
                print(f"Броски d{d_n}: {all_list_damage[i]}")
            d_n += 2

        else: # Специально для Модфикатора урона
            print(f"Модификатор урона: {all_list_damage[i]}")


    print(f"\nОбщий урон: {all_damage}\nСредний урон: {sred_damage}\n")

def dice20(n, bonus, floor, advantage, crit_suc, crit_fail):
    results = []
    success = 0
    crit_success = 0
    failure = 0
    crit_failure = 0
    for i in range(n):
        roll1 = randint(1, 20)
        roll2 = randint(1, 20)
        if advantage == 1:
            if roll1 > roll2:
                roll = roll1
            else:
                roll = roll2
        elif advantage == -1:
            if roll1 > roll2:
                roll = roll2
            else:
                roll = roll1
        else:
            roll = randint(1, 20)

        if roll >= crit_suc:
            stat = "Крит"
            crit_success += 1
        elif roll <= crit_fail:
            stat = "Крит провал"
            crit_failure += 1
        else:
            stat = (roll + bonus)
            if stat >= floor:
                success += 1
            else:
                failure += 1
        results.append(stat)
    print(f"Результаты с бонусами: {results}")
    print(f"Успешные броски:{success}")
    print(f"Критически успешные броски:{crit_success}")
    print(f"Провальные броски:{failure}")
    print(f"Критически провальные броски:{crit_failure}")

def dice_ran_calcul(d_n, dice, list_damage, all_list_damage):
    damage = 0
    for j in range(dice):
        dice_damage = randint(1, d_n)
        list_damage.append(dice_damage)
        damage += dice_damage

    all_list_damage.append(poradok(list_damage))
    return damage

def sred_damage_calcul(d_n, dice):
    return ((d_n + 1)/2) * dice

def poradok(list_damage):
    new_list_damage = []
    for i in range(len(list_damage)):
        new_list_damage.append(max(list_damage))
        list_damage.remove(max(list_damage))

    return new_list_damage

tip = input("Считаем урон или проверки?(d/s)")
if tip == "d":

    dice_rd(0)
    while True:
        quest = input("Хотите ли перебросить кубы? (y/n): ").lower()
        if quest == "y": dice_rd(1)
        elif quest == "n":
            print("Ну и пошел ты")
            break
        else:
            print("Пиши блт правельно")
            continue
elif tip == "s":
    colvo = int(input("скока д20?"))
    plus = int(input("бонус какой?"))
    sloj = int(input("Какая сложность/кд?"))
    adv = int(input("Есть преимущество или помеха?(1/0/-1)"))
    crit20 = int(input("Крит при скольки?"))
    crit1 = int(input("Крит провал при скольки?"))
    dice20(colvo, plus, sloj, adv, crit20, crit1)