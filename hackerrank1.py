import random

# chest1 = ['Bow', 'Sword', 'staff']
#
# while True:
#     if random.choice(chest1) == 'Bow':
#         print('CONGRATS, you\'re an archer!')
#         break
#     elif random.choice(chest1) == 'Sword':
#         print('warrior')
#         break
#     elif random.choice(chest1) == 'staff':
#         print('mage')
#         break



print('Fonsi: Now it\'s time to choose your class!')
player_class = input('would you like to be an "archer", "mage", or "warrior"?')
x = player_class
#
#
# if player_class == "archer":
#     print('YOU HAVE CHOSEN ARCHER. you have been fitted with lvl.1 bow and arrows.''\n')
# elif player_class == "warrior":
#     print('YOU HAVE CHOSEN WARRIOR. you have been fitted with lvl.1 2h sword.''\n')
# elif player_class == "mage":
#     print('YOU HAVE CHOSEN MAGE. you have been fitted with lvl.1 staff.''\n')
#
# print('Fonsi: So you chose {}? Great choice!'.format(player_class))
# print('Fonsi: I\'ll let you have this first chest. In the future you need to a key to unlock chests.''\n')

open_chest = input('PRESS "e" TO OPEN CHEST')

chest_archer = ['bow lvl.2', 'crossbow lvl.2', 'leather coif', 'leather body', 'leather legs']
chest_warrior = ['1h sword lvl.2', '2h sword lvl.2', 'plate helmet', 'plate body', 'plate legs']
chest_mage = ['Great staff lvl.2', 'Apprentice wand lvl.2', 'cloth hood', 'cloth robe', 'cloth shoes']


if open_chest == "e":
    if x == "archer":
        print(random.choice(chest_archer))
    if x == "warrior":
        print(random.choice(chest_warrior))
    if x == "mage"
        print(random.choice(chest_mage))



