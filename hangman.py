from hangman_words import words
import random



def chars_list(word):
    word_list = []
    for i in word:
        word_list.append(i
                         )
    return word_list



def blank_word(word):
    guess = []
    for i in range(len(word)):
        guess.append('-')
    return guess



def print_hangman(status):
    
    if status == 0:
        pass

    elif status == 1:
        print("                    \n                       |\n                       |\n                       |\n                       |\n                       |\n                       |\n                    ————————")
        
    elif status == 2:
        print("                        ________\n                       |        |\n                       |\n                       |\n                       |\n                       |\n                       |\n                    ————————")

    elif status == 3:
        print("                        ________\n                       |        |\n                       |        O\n                       |\n                       |\n                       |\n                       |\n                    ————————")

    elif status == 4:
        print("                        ________\n                       |        |\n                       |        O\n                       |        |\n                       |        |\n                       |\n                       |\n                    ————————")

    elif status == 5:
        print("                        ________\n                       |        |\n                       |        O\n                       |        |\n                       |        |\n                       |       /\n                       |\n                    ————————")

    elif status == 6:
        print("                        ________\n                       |        |\n                       |        O\n                       |        |\n                       |        |\n                       |       / \\\n                       |\n                    ————————")
         
    elif status == 7:
        print("                        ________\n                       |        |\n                       |        O\n                       |       \\|\n                       |        |\n                       |       / \\\n                       |\n                    ————————")

    elif status == 8:
        print("                        ________\n                       |        |\n                       |        O\n                       |       \\|/\n                       |        |\n                       |       / \\\n                       |\n                    ————————")

    
    
while True:
    
    start = input("'s' -> Start game\n'e' -> Exit game\nEnter input: ").lower()

    print()
    
    if start in ['s','e']:
        
        if start == 's':
            
            word_str = random.choice(words)
            word = chars_list(word_str)
            guess = blank_word(word_str)
            total = []
            status = 0

            print("\nGuess the word!\n")
            
            while word != guess and status != 8:
                for i in guess:
                    print(i, end='')

                print()
                
                print_hangman(status)


                while True:
                    
                    inp = input("\nGuess an alphabet in the word: ").lower()
                    
                    if (len(inp) != 1) or (inp not in "abcdefghijklmnopqrstuvwxyz"):
                        print("Enter valid input.")
                        continue
                    
                    else:
                        if inp not in total:
                            
                            total.append(inp)
                            
                            if inp in word:

                                print("\nGreat work! " + inp + " is in the word.\n")
                                
                                for i in range(len(word)):
                                    if inp == word[i]:
                                        guess[i] = inp
                                break
                                
                            else:
                                print("\n" + inp + " is not in the word.\n")
                                status += 1
                                break

                        else:
                            print("\nYou have already used this alphabet.")
                            continue

            if word == guess:
                print("\n\nYOU WIN!\nYou guessed '" + word_str + "' correctly with " + str(8- status) + " tries left.\n\n\n\n")

            if status == 8:
                print_hangman(status)
                print("\n\nYou couldn't guess the word. The word was '" + word_str+"'.\n\n\n\n")

            continue
            
        else:
            print("Exitted game.")
            break

    else:
        print("Enter valid input.\n\n")
        continue
