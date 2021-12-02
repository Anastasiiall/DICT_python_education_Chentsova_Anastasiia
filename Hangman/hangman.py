import random


def start_game():
    print("HANGMAN\nThe game will be available soon.")
    t = 0
    word_list = ['python', 'java', 'javascript', 'php']
    secrets = (random.choice(word_list))
    k = '_' * len(secrets)
    while t <= 7:
        letter = input("" + k + "\nInput a letter:")
        if letter in secrets:
            print('That letter appear in the word')
            b = ''
            for i in range(len(secrets)):
                if letter == secrets[i]:
                    b += letter
                else:
                    b += k[i]
                if b == secrets:
                    print("Your word is", secrets, "\nYou win!\nThanks for playing!")
                    quit()
                if letter in k[i]:
                    print("You have already entered this letter")
                    t -= 1
            k = b
        else:
            print("That letter doesn't appear in the word, used moves " + str(t+1) + " out of 8")
        t += 1
        y = letter
        if y.isalpha():
            print()
        else:
            print("Please enter a lowercase English letter")
            t -= 1
        o = len(letter)
        if o == 1:
            print()
        else:
            print("You should input a single letter")
            t -= 1
        if t == 8:
            print("Your word is", secrets, "\nYou lose!\nThanks for playing!")
            break


def game_1():
    n = input('Type "play" to play the game, "exit" to quit:')
    if n == "play":
        start_game()
    elif n == "exit":
        return game_1()
    else:
        return game_1()


game_1()
