from random import randint

print("Добро пожаловать солага, здесь ты можешь считать урон по быстренькому :D")
d4 = int(input("Кооличество d4: "))
d6 = int(input("Кооличество d6: "))
d8 = int(input("Кооличество d8: "))
d10 = int(input("Кооличество d10: "))
d12 = int(input("Кооличество d12: "))
d20 = int(input("Кооличество d20: "))
mod = int(input("Модификатор урона: "))
all_damage = 0
list_damage = list()

if d4 != 0:
    list_damage.append("d4:")
    for i in range(d4):
        x = randint(1,4)
        list_damage.append(x)
        all_damage += x

if d6 != 0:
    list_damage.append("d6:")
    for i in range(d6):
        x = randint(1,6)
        list_damage.append(x)
        all_damage += x

if d8 != 0:
    list_damage.append("d8:")
    for i in range(d8):
        x = randint(1,8)
        list_damage.append(x)
        all_damage += x

if d10 != 0:
    list_damage.append("d10:")
    for i in range(d10):
        x = randint(1,10)
        list_damage.append(x)
        all_damage += x

if d12 != 0:
    list_damage.append("d12:")
    for i in range(d12):
        x = randint(1,12)
        list_damage.append(x)
        all_damage += x

if d20 != 0:
    list_damage.append("d20:")
    for i in range(d20):
        x = randint(1,20)
        list_damage.append(x)
        all_damage += x

if mod != 0:
    list_damage.append("+ " + str(mod))
    all_damage += mod

print(list_damage, all_damage)



