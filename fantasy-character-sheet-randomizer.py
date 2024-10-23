import math
import random

# initialize random module
seed = int(input('Enter a number to generate a seed: '))
random.seed(seed)

random_num = random.random()

# split random num into useable digits
usable_seed = str(math.floor(random_num * (10 ** 15)))
seed_listed = list(usable_seed)

# traits dict
traits = {
    'race' : ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human', 'Tiefling'],
    'classing' : ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard'],
    'principle' : ['Lawful', 'Neutral', 'Chaotic'], 
    'morality' : ['Good', 'Neutral', 'Evil'],
    'deity' : ['Somnius', 'Muthgag', 'Thyrmus', 'Jairus', 'Seref', 'Errgesh', 'Mundu', 'Yrrethyl', 'Tempes', 'Onis'],
}

### character gen ###
# race
race_ID = int(seed_listed[0])
if race_ID < 9:
    race = traits['race'][race_ID]
elif race_ID == 9:
    new_race_ID = random.randrange(0, 8)
    race = traits['race'][new_race_ID]

# class
class_ID = int(seed_listed[1])
if class_ID <= 3:
    new_class_ID = random.randrange(0, 11, 1)
    classing = traits['classing'][new_class_ID]
elif 4 <= class_ID <= 7:
    new_class_ID = random.randrange(0, 11, 2)
    classing = traits['classing'][new_class_ID]
elif 8 <= class_ID <= 11:
    new_class_ID = random.randrange(0, 11, 3)
    classing = traits['classing'][new_class_ID]

# principle
principle_ID = int(seed_listed[2])
if principle_ID <= 3:
    principle = traits['principle'][0]
elif 4 <= principle_ID <= 7:
    principle = traits['principle'][1]
elif 8 <= principle_ID <= 11:
    principle = traits['principle'][2]
    
# morality
morality_ID = int(seed_listed[3])
if morality_ID <= 3:
    morality = traits['morality'][0]
elif 4 <= morality_ID <= 7:
    morality = traits['morality'][1]
elif 8 <= morality_ID <= 11:
    morality = traits['morality'][2]

# deity
deity_ID = int(seed_listed[4])
if deity_ID <= 3:
    new_deity_ID = random.randrange(0, 9, 1)
    deity = traits['deity'][new_deity_ID]
elif 4 <= deity_ID <= 7:
    new_deity_ID = random.randrange(0, 9, 2)
    deity = traits['deity'][new_deity_ID]
elif 8 <= deity_ID <= 10:
    new_deity_ID = random.randrange(0, 9, 3)
    deity = traits['deity'][new_deity_ID]

### stats ###
fivestat_array= []

print('\n{<>} Stat Rolls {<>}')

# strength stat
str_array = []
str_rolls = 4
while str_rolls != 0:
    str_array.append(random.randrange(1,7))
    str_rolls -= 1
str_array.remove(min(str_array))
print(f'STR: {str_array}')
strength = sum(str_array)
# str floor/ceiling
if strength < 6:
    strength = 6
if strength > 16:
    strength = 16
fivestat_array.append(strength)

# dexterity stat
dex_array = []
dex_rolls = 4
while dex_rolls != 0:
    dex_array.append(random.randrange(1,7))
    dex_rolls -= 1
dex_array.remove(min(dex_array))
print(f'DEX: {dex_array}')
dexterity = sum(dex_array)
# dex floor/ceiling
if dexterity < 6:
    dexterity = 6
if dexterity > 16:
    dexterity = 16
fivestat_array.append(dexterity)

# constitution stat
con_array = []
con_rolls = 4
while con_rolls != 0:
    con_array.append(random.randrange(1,7))
    con_rolls -= 1
con_array.remove(min(con_array))
print(f'CON: {con_array}')
constitution = sum(con_array)
# con floor/ceiling
if constitution < 6:
    constitution = 6
if constitution > 16:
    constitution = 16
fivestat_array.append(constitution)

# intelligence stat
int_array = []
int_rolls = 4
while int_rolls != 0:
    int_array.append(random.randrange(1,7))
    int_rolls -= 1
int_array.remove(min(int_array))
print(f'INT: {int_array}')
intelligence = sum(int_array)
# int floor/ceiling
if intelligence < 6:
    intelligence = 6
if intelligence > 16:
    intelligence = 16
fivestat_array.append(intelligence)

# wisdom stat
wis_array = []
wis_rolls = 4
while wis_rolls != 0:
    wis_array.append(random.randrange(1,7))
    wis_rolls -= 1
wis_array.remove(min(wis_array))
print(f'WIS: {wis_array}')
wisdom = sum(wis_array)
# wis floor/ceiling
if wisdom < 6:
    wisdom = 6
if wisdom > 16:
    wisdom = 16
fivestat_array.append(wisdom)

# charisma stat
fivestat_total = sum(fivestat_array)
charisma = 72 - fivestat_total

# write results to text file
with open('character_sheet.txt', 'w') as file:
    file.write('{<>} Stat Rolls {<>}\n')
    file.write(f'STR: {str_array}\n')
    file.write(f'DEX: {dex_array}\n')
    file.write(f'CON: {con_array}\n')
    file.write(f'INT: {int_array}\n')
    file.write(f'WIS: {wis_array}\n\n')


    file.write('{@} Character Sheet {@}\n')
    file.write(f'Race: {race}\n')
    file.write(f'Class: {classing}\n')
    if (principle != 'Neutral') and (morality != 'Neutral'):
        file.write(f'Alignment: {principle} {morality}\n')
    else:
        file.write(f'Alignment: True Neutral\n')
    file.write(f'Affiliation: Cult of {deity}\n')
    file.write(f'STR: {strength}\n')
    file.write(f'DEX: {dexterity}\n')
    file.write(f'CON: {constitution}\n')
    file.write(f'INT: {intelligence}\n')
    file.write(f'WIS: {wisdom}\n')
    file.write(f'CHA: {charisma}\n')
file.close()

# display randomizer output
print('\n{@} Character Sheet {@}')
print(f'Race: {race}')
print(f'Class: {classing}')
if (principle != 'Neutral') and (morality != 'Neutral'):
    print(f'Alignment: {principle} {morality}')
else:
    print(f'Alignment: True Neutral')
print(f'Affiliation: Cult of {deity}')
print(f'STR: {strength}')
print(f'DEX: {dexterity}')
print(f'CON: {constitution}')
print(f'INT: {intelligence}')
print(f'WIS: {wisdom}')
print(f'CHA: {charisma}')