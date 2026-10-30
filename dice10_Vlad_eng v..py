from random import randint # Random
print("Welcome, comrade! Here you can quickly calculate your damage ::D")
dice_dict = dict()

def dice_rd(n): # Damage rolls
    all_list_damage = list()
    all_damage = 0
    sred_damage = 0
    d_n = 4

    if n == 0: # The first version of the function, used when values ​​are being entered for the first time
        for i in range(1,7):
            list_damage = []
            dice = int(input(f"Amount d{d_n}: "))
            all_damage += dice_ran_calcul(d_n, dice, list_damage, all_list_damage)
            sred_damage += sred_damage_calcul(d_n, dice)
            dice_dict[d_n] = dice
            d_n += 2

        mod = int(input("Damage modifier: "))
        all_list_damage.append("+ "+str(mod))
        all_damage += mod
        sred_damage += mod
        dice_dict[21] = mod


    else: # The second version of the function, for re-rolling the dice
        for i,j in dice_dict.items():
            list_damage = []
            if i < 20:
                all_damage += dice_ran_calcul(i, j, list_damage, all_list_damage)
                sred_damage += sred_damage_calcul(i, j)

            elif i == 21:
                all_damage += j
                sred_damage += j
                all_list_damage.append("+ "+str(j))


    print("\n----Conclusion----")
    d_n = 4
    for i in range(len(all_list_damage)):
        if i <= 4: # Especially for d4,6,8,10,12
            if len(all_list_damage[i]) == 0: # If no bets were placed in Dice, it won’t appear in the withdrawal section.
                d_n += 2
                continue
            else:
                print(f"Throws d{d_n}: {all_list_damage[i]}")
            d_n += 2

        elif i == 5: # Especially for d20
            if len(all_list_damage[i]) == 0: # If no bets were placed in Dice, it won’t appear in the withdrawal section.
                continue
            else:
                print(f"To-hit rolls d20: {all_list_damage[i]}")

        else: # Specifically for the Damage Modifier
            print(f"Damage modifier: {all_list_damage[i]}")

    print(f"\nTotal damage: {all_damage}\nAverage damage: {sred_damage}\n")

def dice20(): # A separate function that rolls a d20 for attacks or for overcoming difficulty checks.
    n = int(input("Quantity d20: "))
    bonus = int(input("Bonus to check/attack: "))
    floor = int(input("Difficulty/cd: "))
    advantage = int(input("Is there an advantage or a hindrance? (2/1/0/-1/-2): "))
    crit20 = int(input("The importance of critical success in: "))
    crit1 = int(input("The significance of critical failure at: "))

    results = []
    success = 0
    crit_success = 0
    failure = 0
    crit_failure = 0

    for i in range(n):
        roll_list = []
        for j in range(advantage + 1): # Advantages and obstacles
            roll_list.append(randint(1,20))
        
        if advantage >= 0: roll = max(roll_list)
        elif advantage < 0: roll = min(roll_list)

        if roll >= crit20: # Value
            crit_success += 1
        elif roll <= crit1:
            crit_failure += 1
        else:
            if roll + bonus >= floor:
                success += 1
            else:
                failure += 1
        results.append(roll + bonus)
        results = poradok(results)

    print("\n-----Conclusion-----")
    print(f"Results with bonuses: {results}")
    print(f"Successful throws:{success}")
    print(f"Critically successful rolls:{crit_success}")
    print(f"Failed throws:{failure}")
    print(f"Critically failed rolls:{crit_failure}")

def dice_ran_calcul(d_n, dice, list_damage, all_list_damage): #Rolls a die to get a random value
    damage = 0
    for j in range(dice):
        dice_damage = randint(1, d_n)
        list_damage.append(dice_damage)
        damage += dice_damage

    all_list_damage.append(poradok(list_damage))
    if d_n != 20:
        return damage

def sred_damage_calcul(d_n, dice): # Calculates the average damage for a specific die
    return ((d_n + 1)/2) * dice

def poradok(list_damage): # Sorts the numbers that appear into order - from maximum to minimum - using bubble sort
    new_list_damage = []
    for i in range(len(list_damage)):
        new_list_damage.append(max(list_damage))
        list_damage.remove(max(list_damage))
    return new_list_damage

def module(num): # Module function
    if num >= 0: return num 
    else: return -num

while True: # Script
    tip = input("Calculating damage or checks/attacks (d/s): ")
    if tip == "d":
        dice_rd(0)
        while True:
            quest = input("Do you want to reroll the dice?? (y/n): ").lower()
            if quest == "y": dice_rd(1)
            elif quest == "n":
                print("Well, screw you then.")
                break
            else:
                print("Learn to write correctly, damn it.")
                continue
    elif tip == "s": dice20()