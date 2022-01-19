import re


def start():
    print()
    print('----------------------')
    print('    TicTacToe Game    ')
    print('----------------------')
    print('     How to play:     ')
    print('  x - number of str   ')
    print(' y - number of column ')
    print()

def showfield():
    print('    0   1   2  ')

    for i in range(3):
        print(f'{i} | {field[i][0]} | {field[i][1]} | {field[i][2]} |')

def motion():
    while True:
        coords = input("    Input x and y: ").split() 

        if len(coords) != 2:
            print()
            print("You need two coords to make a move")
            print()
            continue

        x, y = coords
        
        if not (x.isdigit() and y.isdigit()):
            print()
            print("Input numbers instead of mess")
            print()
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or  y < 0 or  y > 2 :
            print()
            print("Incorrect coords! x in [0, 2], y in [0, 2]")
            print()
            continue

        if field[x][y] != ' ':
            print()
            print("This field is already filled")
            print()
            continue
        
        print()
        print('------------------------------')
        print(f"Your decision: {x} str, {y} colomn")
        print()

        return x, y

def victory():
    def check_for(item):
        if ((field[0][0] == item and field[0][1] == item and field[0][2] == item ) or 
            (field[1][0] == item and field[1][1] == item and field[1][2] == item ) or 
            (field[2][0] == item and field[2][1] == item and field[2][2] == item ) or
            (field[0][0] == item and field[1][0] == item and field[2][0] == item ) or
            (field[0][1] == item and field[1][1] == item and field[2][1] == item ) or 
            (field[0][2] == item and field[1][2] == item and field[2][2] == item ) or 
            (field[0][0] == item and field[1][1] == item and field[2][2] == item ) or  
            (field[0][2] == item and field[1][1] == item and field[2][0] == item )):
            return True
        return False

    if (check_for('X')):
        print("Tic wins")
        return True

    if (check_for('0')):
        print("Tac wins")
        return True

    return False

start()
field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
turn = 0

while True: 
    turn += 1
    showfield() 

    if turn % 2 == 1:
        print()
        print(" Tic turn [X]      ↓")
    else:
        print()
        print(" Tac turn [0]      ↓")

    x, y = motion()

    if turn % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if victory():
        showfield()
        break
    
    if turn == 9:
        showfield()
        print("Draw")
        break