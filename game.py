# game.py

def play():
    print('bleh')

print('Hello, please enter your name...')
name = input()

print('Hello ' + name + ', enter y to continue and n to quit')
choice = input()

if choice == 'y' :
    print('Lets play')
    play()
elif choice == 'n' :
    print('Bye')
    exit()
