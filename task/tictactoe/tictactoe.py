# write your code here
# board = f"
# ---------
# | O _ O |
# | X X O |
# | _ X X |
# ---------"


def win(i):
    if (i[0] == i[3] == i[6] and i[1] == i[4] == i[7]) or \
            (i.count('O') - i.count('X') > 1 or i.count('X') - i.count('O') > 1):
        print("Impossible")
    else:
        if i[0] == i[1] == i[2]:  # Top
            print(f"{i[0]} wins")
        elif i[3] == i[4] == i[5]:  # Middle
            print(f"{i[3]} wins")
        elif i[6] == i[7] == i[8]:  # Bottom
            print(f"{i[6]} wins")
        elif i[0] == i[4] == i[8]:  # Diagonal Right
            print(f"{i[0]} wins")
        elif i[2] == i[4] == i[6]:  # Diagonal Left
            print(f"{i[2]} wins")
        elif i[0] == i[3] == i[6]:  # Down Right
            print(f"{i[0]} wins")
        elif i[1] == i[4] == i[7]:  # Down Middle
            print(f"{i[1]} wins")
        elif i[2] == i[5] == i[8]:  # Down Left
            print(f"{i[2]} wins")
        else:
            if '_' not in i:
                print("Draw")
            else:
                print('Game not finished')


def trans_index(a, b):
    # (1, 3) (2, 3) (3, 3)
    # (1, 2) (2, 2) (3, 2)
    # (1, 1) (2, 1) (3, 1)

    if a == 1 and b == 3:
        return 0
    elif a == 2 and b == 3:
        return 1
    elif a == 3 and b == 3:
        return 2
    elif a == 1 and b == 2:
        return 3
    elif a == 2 and b == 2:
        return 4
    elif a == 3 and b == 2:
        return 5
    elif a == 1 and b == 1:
        return 6
    elif a == 2 and b == 1:
        return 7
    else:
        return 8


def check_range(a, b):
    return int(a) < 4 and int(b) < 4


# def check_field(a, b):
#     return


def print_board(bd):
    d = '-' * 9
    board = f"{d}\n| {bd[0]} {bd[1]} {bd[2]} |\n| {bd[3]} {bd[4]} " \
            f"{bd[5]} |\n| {bd[6]} {bd[7]} {bd[8]} |\n{d}"
    print(board)


inp = '_'*9
print_board(inp)
game = False
turn = 0

while not game:
    inp2 = input().split()

    if not "".join(inp2).isdigit():
        print("You should enter numbers!")
        continue
    elif not check_range(inp2[0], inp2[1]):
        print("Coordinates should be from 1 to 3!")
        continue
    elif inp[trans_index(int(inp2[0]), int(inp2[1]))] in 'XO':
        print("This cell is occupied! Choose another one!")
        continue
    else:
        idx = trans_index(int(inp2[0]), int(inp2[1]))
        user = 'X' if turn % 2 == 0 else 'O'
        turn = turn + 1

    new_ = [x for x in inp]
    new_[idx] = user
    inp = "".join(new_)

    print_board(inp)

    if "_" not in inp:
        win(inp)
        game = True
