import random


def start_game():
    print("HANGMAN\nThe game will be available soon.")
    t = 0
    word_list = ['python', 'java', 'javascript', 'php']
    secrets = (random.choice(word_list))
    line = '_' * len(secrets)
    word = input("" + line + "\nInput a letter:")
    while t <= 7:
        if word in secrets:
            print("That letter appear in the word")
            n = ''
            for i in range(len(secrets)):
                if word == secrets[i]:
                    n += word
                else:
                    n += line[i]
                if n == secrets:
                    print("Your word is", secrets, "\nYou win!\nThanks for playing!")
                    quit()
                if word in line[i]:
                    print("You have already entered this letter")
                    t -= 1
            line = n
        else:
            print("That letter doesn't appear in the word" + "\nNumber of mistakes:" + str(t) + " out of 7")
        t += 1
        y = word
        if y.isalpha():
            print()
        else:
            print("Please enter a lowercase English letter")
            t -= 1
        o = len(word)
        if o == 1:
            print()
        else:
            print("You should input a single letter")
            t -= 1
        if t == 8:
            print("Your word is", secrets, "\nYou lose!\nThanks for playing!")
        break


def game_1():
    k = input('Type "play" to play the game, "exit" to quit:')
    if k == "play":
        start_game()
    elif k == "exit":
        return game_1()
    else:
        return game_1()


game_1()
