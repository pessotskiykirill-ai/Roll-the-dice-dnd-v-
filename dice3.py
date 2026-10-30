from random import randint

print("Добро пожаловать солага, здесь ты можешь считать урон по быстренькому :D")

d4 = int(input("Количество d4: "))
d6 = int(input("Количество d6: "))
d8 = int(input("Количество d8: "))
d10 = int(input("Количество d10: "))
d12 = int(input("Количество d12: "))
d20 = int(input("Количество d20: "))
mod = int(input("Модификатор урона: "))

all_damage = 0
damage_rolls = []

def rolldice(count, sides):
    rolls = []
    total = 0
    for i in range(count):
        x = randint(1, sides)
        rolls.append(x)
        total += x
    return rolls, total

for dice, sides in [(d4, 4), (d6, 6), (d8, 8), (d10, 10), (d12, 12)]:
    rolls, total = rolldice(dice, sides)
    damage_rolls.extend(rolls)
    all_damage += total

all_damage += mod

d20_rolls, d20_total = rolldice(d20, 20)

print("\n--- выводы---")
print("Бросок d20:", d20_rolls, "| Сумма:", d20_total)
print("Урон:", damage_rolls, "+", mod, "| Итого:", all_damage)