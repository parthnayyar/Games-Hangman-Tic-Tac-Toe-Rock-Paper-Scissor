positions=['TL','T','TR','L','M','R','BL','B','BR'] # name of positions in board


def print_board(): # prints the board
    print('\n\n'+b[0]+'|'+b[1]+'|'+b[2]+'\n'+b[3]+'|'+b[4]+'|'+b[5]+'\n'+b[6]+'|'+b[7]+'|'+b[8]+'\n')


def game_end(): # checks and returns the winner's name. If game hasn't been won by anyone, returns false
    if b[0]==b[1]==b[2]!='—':   # top row
        return b[0]
    elif b[3]==b[4]==b[5]!='—': # middle row
        return b[3]
    elif b[6]==b[7]==b[8]!='—': # bottom row
        return b[6]
    elif b[0]==b[3]==b[6]!='—': # left column
        return b[0]
    elif b[1]==b[4]==b[7]!='—': # middle column
        return b[1]
    elif b[2]==b[5]==b[8]!='—': # right column
        return b[2]
    elif b[0]==b[4]==b[8]!='—': # diagonal \
        return b[0]
    elif b[2]==b[4]==b[6]!='—': # diagonal /
        return b[2]
    else:                       # no winner      
        return False


def tie(): # checks if game is tied
    for i in b: 
        if i=='—':
            return False
    else:
        return True


def pos_convertor(pos): # converts the string-type position into the equivalent index-type position
    if pos=='TL':
        return 0
    elif pos=='T':
        return 1
    elif pos=='TR':
        return 2
    elif pos=='L':
        return 3
    elif pos=='M':
        return 4
    elif pos=='R':
        return 5
    elif pos=='BL':
        return 6
    elif pos=='B':
        return 7
    else:
        return 8


def play_turn(player): # plays a turn
    while True:
        inp=input(player+"'s turn: ").upper()
        if inp in positions:
            if b[pos_convertor(inp)]=='—':
                b[pos_convertor(inp)]=player
                break
            else:
                print("That position is already taken. Try again.\n")
                continue
        else:
            print("Enter valid input.\n")
            continue


print("Welcome to Tic—Tac—Toe!\n")
print("How to play:\nEnter position you want your symbol on in the form of:")
print("  TL -> Top Left")
print("  T -> Top")
print("  TR -> Top Right")
print("  L -> Left")
print("  M -> Middle")
print("  R -> Right")
print("  BL -> Bottom Left")
print("  B -> Bottom")
print("  BR -> Bottom Right")
inp=''


while inp!='end':
    b=['—','—','—','—','—','—','—','—','—'] # defining empty board
    counter=0 # defining counter to help switch turns
    while game_end() is False:
        if tie():
            print_board()
            print('The game was tied.')
            break
        else:
            print_board()
            if counter%2==0:
                play_turn('X')
                counter+=1
            else:
                play_turn('O')
                counter+=1


    if game_end()!=False:
        print_board()
        print(game_end(),'won the game.')


    inp=input("\nEnter anything to play again or type 'end' to stop playing: ").lower()
