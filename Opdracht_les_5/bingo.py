# We hebben de random module nodig om willekeurige getallen te genereren
import random
# Totaal aantal getallen op de kaart zal hoogte x breedte zijn
bingo_number_total = 4 ** 2
# Daarna maken we een lijst met 99 getallen waar we uit gaan kiezen
numbers_all = list(range(1, 100))
# We gooien alle ballen door elkaar
random.shuffle(numbers_all)
# ..en pakken de eerste 16 getallen
bingo_numbers = numbers_all[:bingo_number_total]

card = []
row = []
for number in bingo_numbers:
    row.append(number)
    if len(row) > 3:
        card.append(row)
        row = []

for row in card:
    print(row)
print()

random.shuffle(numbers_all)
crossed_numbers = numbers_all[:50]

for row in card:
    for number in row:
        if number in crossed_numbers:
            index = row.index(number)
            row[index] = "X"

for row in card:
    print(row)
print()

for row in card:
    bingo_in_row = True
    for number in row:
        if number != "X":
            bingo_in_row = False
    if bingo_in_row:
        print("Je hebt een bingo horizontaal")

#print(card[0][0])
for col in range(0, 4):
    bingo_in_col = True
    for row in card:
        if row[col] != "X":
            bingo_in_col = False
    if bingo_in_col:
        print("Je hebt een bingo verticaal")