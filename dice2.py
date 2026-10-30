from random import randint
print("Добро пожаловать солага, здесь ты можешь считать урон по быстренькому :D")

def dice_rd():
    all_list_damage = list()
    all_damage = 0
    d_n = 4
    for i in range(1,7):    
        if d_n <= 12: # Условия для d4,6,8,10,12
            list_damage = [f"d{d_n}:"]
            dice = int(input(f"Количество d{d_n}: "))
            if dice > 0:
                for j in range(dice):
                    dice_damage = randint(1, d_n)
                    list_damage.append(dice_damage)
                    all_damage += dice_damage

                all_list_damage.append(list_damage)
            d_n += 2

        else: # Отдельные условие для d20
            list_damage = [f"d{20}:"]
            dice = int(input(f"Количество d{20}: "))
            if dice > 0:
                for j in range(dice):
                    dice_damage = randint(1, 20)
                    list_damage.append(dice_damage)
                    all_damage += dice_damage

                all_list_damage.append(list_damage)
    
    mod = int(input("Модификатор урона: "))
    if mod > 0:
        all_list_damage.append(" + "+str(mod))
        all_damage += mod
    
    print("----Вывод----")
    for i in all_list_damage:
        print(i, end="")
    print(f"\nОбщий урон: {all_damage}")

dice_rd()