from random import randint
print("Добро пожаловать солага, здесь ты можешь считать урон по быстренькому :D")
dice_dict = dict()

def dice_rd(n):
    all_list_damage = list()
    all_damage = 0
    sred_damage = 0
    d_n = 4

    if n == 0:
        dice20 = int(input("Кубы d20 на попадание: "))
        plus_popad = int(input("Плюс к попаданию: "))

        print("Урон в кубах от одной атаки: ")
        for j in range(dice20):
            for i in range(1,6):
                list_damage = []
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








def dice_ran_calcul(d_n, dice, list_damage, all_list_damage):
    damage = 0
    for j in range(dice):
        dice_damage = randint(1, d_n)
        list_damage.append(dice_damage)
        damage += dice_damage

    all_list_damage.append(poradok(list_damage))
    if d_n != 20:
        return damage

def sred_damage_calcul(d_n, dice):
    return ((d_n + 1)/2) * dice

def poradok(list_damage):
    new_list_damage = []
    for i in range(len(list_damage)):
        new_list_damage.append(max(list_damage))
        list_damage.remove(max(list_damage))
    
    return new_list_damage