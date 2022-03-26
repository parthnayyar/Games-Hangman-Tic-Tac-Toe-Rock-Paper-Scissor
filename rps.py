import random
import time


print("Welcome to Rock Papers Scissors")


while True:
    inp = input("\n'P' -> Play\n'E' -> Exit\n")
    if inp.lower() in ['p','e']:
        if inp.lower() == 'p':
            while True:
                rpsinp = input("\n'R' -> Rock\n'P' -> Paper\n'S' -> Scissors\n")
                if rpsinp.lower() == 'r':
                    rpsinp = 'Rock'
                elif rpsinp.lower() == 'p':
                    rpsinp = 'Paper'
                elif rpsinp.lower() == 's':
                    rpsinp = 'Scissors'
                else:
                    print('Enter a valid input\n')
                    continue	
                rpscomp = random.choice(['Rock','Paper','Scissors'])
                print('Computer:',rpscomp)
                time.sleep(1)
                if rpsinp == rpscomp:
                    print("Draw")
                    continue
                elif ((rpsinp == 'Rock' and rpscomp == 'Scissors') or
                     (rpsinp == 'Paper' and rpscomp == 'Rock') or
                     (rpsinp == 'Scissors' and rpscomp == 'Papers')):
                    print('You win!')
                    break
                else:
                    print('You lose!')
                    break                
        else:
            print('Exitted game')
            break
    else:
        print('Enter a valid input\n\n')
        continue
