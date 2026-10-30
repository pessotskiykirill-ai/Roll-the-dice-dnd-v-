from random import randint
print("Добро пожаловать солага, здесь ты можешь считать урон по быстренькому :D")

def dice_rd():
    all_list_damage = list()
    all_damage = 0
    d_n = 4
    for i in range(1,7):
        list_damage = []
        if d_n <= 12: # Условия для d4,6,8,10,12
            dice = int(input(f"Количество d{d_n}: "))
            for j in range(dice):
                dice_damage = randint(1, d_n)
                list_damage.append(dice_damage)
                all_damage += dice_damage

            all_list_damage.append(list_damage)
            d_n += 2

        else: # Отдельные условие для d20
            dice = int(input(f"Количество d{20}: "))
            for j in range(dice):
                dice_damage = randint(1, 20)
                list_damage.append(dice_damage)
                all_damage += dice_damage

            all_list_damage.append(list_damage)
    
    mod = int(input("Модификатор урона: "))
    all_list_damage.append("+ "+str(mod))
    all_damage += mod

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

        elif i == 5: # Специально для d20
            if len(all_list_damage[i]) == 0: # Если для дайс не кидали, то он не попадется в вкладку вывод
                continue
            else:
                print(f"Броски d20: {all_list_damage[i]}")

        else: # Специально для Модфикатора урона
            print(f"Модификатор урона: {all_list_damage[i]}")

    print(f"\nОбщий урон: {all_damage}\n")

dice_rd()