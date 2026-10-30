from random import randint
print("Добро пожаловать солага, здесь ты можешь считать урон по быстренькому :D")
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
                all_damage += dice_ran_calcul(d_n, dice, list_damage, all_list_damage, 0, 0)
                sred_damage += sred_damage_calcul(d_n, dice)
                dice_dict[d_n] = dice
                d_n += 2

            else: # Отдельные условие для d20
                plus_atacks = int(input("\nПлюс к попаданию: "))
                
                dice = int(input(f"Количество d{20} на попадание: "))
                dice_ran_calcul(20, dice, list_damage, all_list_damage, plus_atacks, 1)
                sred_damage_calcul(20, dice)
                dice_dict[20] = dice
                dice_dict[22] = plus_atacks
        
        mod = int(input("Модификатор урона: "))
        all_list_damage.append("+ "+str(mod))
        all_damage += mod
        sred_damage += mod
        dice_dict[21] = mod


    else: # Второй варинт функции, для переброса кубов
        for i,j in dice_dict.items():
            list_damage = []
            if i < 20: 
                all_damage += dice_ran_calcul(i, j, list_damage, all_list_damage, 0, 0)
                sred_damage += sred_damage_calcul(i, j)

            elif i == 20:
                dice_ran_calcul(i, j, list_damage, all_list_damage, dice_dict[22], 1)

            elif i == 21: 
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

        elif i == 5: # Специально для d20
            if len(all_list_damage[i]) == 0: # Если для дайс не кидали, то он не попадется в вкладку вывод
                continue
            else:
                print(f"Броски d20: {all_list_damage[i]}")

        else: # Специально для Модфикатора урона
            print(f"Модификатор урона: {all_list_damage[i]}")


    print(f"\nОбщий урон: {all_damage}\nСредний урон: {sred_damage}\n")


def dice_ran_calcul(d_n, dice, list_damage, all_list_damage, plus_atacks, n):
    if n == 0: # Для бросков к урону
        damage = 0
        for j in range(dice):
            dice_damage = randint(1, d_n)
            list_damage.append(dice_damage)
            damage += dice_damage
        
        all_list_damage.append(poradok(list_damage))
        return damage

    else: # Для бросков к попаданию
        for j in range(dice):
            dice_damage = randint(1, d_n)
            list_damage.append(dice_damage)
        
        list_damage = poradok(list_damage)
        for i in range(len(list_damage)):
            list_damage[i] = str(list_damage[i]) + " : " + str(list_damage[i] + plus_atacks)
        
        all_list_damage.append(list_damage)


def sred_damage_calcul(d_n, dice):
    return ((d_n + 1)/2) * dice

def poradok(list_damage):
    new_list_damage = []
    for i in range(len(list_damage)):
        new_list_damage.append(max(list_damage))
        list_damage.remove(max(list_damage))
    
    return new_list_damage


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