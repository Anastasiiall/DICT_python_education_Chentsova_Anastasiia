board = list(range(1,10))

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)

def take_input(player_t):
    val = False
    while not val:
        player_an = int(input("Enter the coordinate " + player_t + ":"))

        if player_an >= 1 and player_an <= 9:
            if str(board[player_an-1]) not in "XO":
                board[player_an - 1] = player_t
                val = True

            else:
                print("This cell is occupied! Choose another one!")

        else:
            print("You should enter numbers!")


def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    win = False
    c = 0
    while not win:
        draw_board(board)
        if c % 2 == 0:
            take_input("X")
        else:
            take_input("O")

        c += 1

        if c > 4:
            t = check_win(board)
            if t:
                win = True
                print(t,"wins!")
                break

        if c == 9:
            print("Impossible!")
            break

    draw_board(board)

main(board)

