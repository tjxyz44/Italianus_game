print('\n')
print('Fonsi: Hello, Welcome to the world of italianus, My name is Fonsi, I will be your guide through this journey.')
print("Please tell me your name:"'\n')

name_input = input('Enter your name. 5 character limit. ')
player_name = name_input

while True:
        if len(name_input) <= 5:
                print("cool name {}!"'\n'.format(name_input))
                break
        name_input = input("Invalid, Try Again. Enter your name. 5 character limit.")

print('Fonsi: first off {}, let\'s get you moving.'.format(name_input))
movement_input = input('To move around press "w" to go forward, "a" for left, "s" for back, "d" for right. Go ahead and try it!')

if movement_input == "w":
        print('PLAYER MOVES FORWARD''\n')
elif movement_input == "a":
        print('PLAYER MOVES LEFT''\n')
elif movement_input == "s":
        print('PLAYER MOVES BACK''\n')
elif movement_input == "d":
        print('PLAYER MOVES RIGHT''\n')

print('Fonsi: Great work! now move forward 2 spaces, and left 1 space to talk to me again!')
movement_input = input('Press "w" to go forward, "a" for left, "s" for back, "d" for right.')


while True:
        if movement_input == "w":
                print('PLAYER MOVES FORWARD')
                break
        input('WRONG WAY, TRY AGAIN')

movement_input = input('Press "w" to go forward, "a" for left, "s" for back, "d" for right.')

while True:
        if movement_input == "w":
                print('PLAYER MOVES FORWARD')
                break
        input('WRONG WAY, TRY AGAIN')

movement_input = input('Press "w" to go forward, "a" for left, "s" for back, "d" for right.')

while True:
        if movement_input == "a":
                print('PLAYER MOVES LEFT''\n')
                break
        input('WRONG WAY, TRY AGAIN')

print('Fonsi: Well hello again {}! Seems like you got moving down pretty well!'.format(player_name))



