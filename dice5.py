from random import randint
print("Добро пожаловать солага, здесь ты можешь считать урон по быстренькому :D")
dice_dict = dict()

def dice_rd(n):
    all_list_damage = list()
    all_damage = 0
    d_n = 4

    if n == 0: # Первый варинат функции, когда набираются первый раз значения
        for i in range(1,7):
            list_damage = []
            if d_n <= 12: # Условия для d4,6,8,10,12
                dice = int(input(f"Количество d{d_n}: "))
                all_damage += dice_ran_calcul(d_n, dice, list_damage, all_list_damage)
                dice_dict[d_n] = dice
                d_n += 2

            else: # Отдельные условие для d20
                dice = int(input(f"Количество d{20}: "))
                all_damage += dice_ran_calcul(20, dice, list_damage, all_list_damage)
                dice_dict[20] = dice
        
        mod = int(input("Модификатор урона: "))
        all_list_damage.append("+ "+str(mod))
        all_damage += mod
        dice_dict[21] = mod


    else: # Второй варинт функции, для переброса кубов
        for i,j in dice_dict.items():
            list_damage = []
            if i != 21: all_damage += dice_ran_calcul(i, j, list_damage, all_list_damage)
            else: 
                all_damage += j 
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


    print(f"\nОбщий урон: {all_damage}\n")


def dice_ran_calcul(d_n, dice, list_damage, all_list_damage):
    damage = 0
    for j in range(dice):
        dice_damage = randint(1, d_n)
        list_damage.append(dice_damage)
        damage += dice_damage

    all_list_damage.append(list_damage)
    return damage


dice_rd(0)
while True:
    quest = input("Хотите ли перебросить кубы? (y/n):").lower()
    if quest == "y": dice_rd(1)
    elif quest == "n": 
        print("Ну и пошел ты")
        break
    else: 
        print("Пиши блт правельно")
        continue