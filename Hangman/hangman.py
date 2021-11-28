import random


def start_game():
    print("HANGMAN\nThe game will be available soon.")
    t = 0
    word_list = ['python', 'java', 'javascript', 'php']
    secrets = (random.choice(word_list))
    word = '_' * len(secrets)
    while t <= 7:
        a = input("" + word + "\nInput a letter:")
        if a in secrets:
            print("That letter appear in the word")
            v = ''
            for i in range(len(secrets)):
                if a == secrets[i]:
                    v += a
                else:
                    v += word[i]
                if v == secrets:
                    print("Your word is", secrets, "\nYou win!\nThanks for playing!")
                    quit()
                if a in word[i]:
                    print("You have already entered this letter")
                    t -= 1
            word = v
        else:
            print("That letter doesn't appear in the word" + "\nNumber of mistakes:" + str(t) + " out of 7")
        t += 1
        y = a
        if y.isalpha():
            print()
        else:
            print("Please enter a lowercase English letter")
            t -= 1
        k = len(a)
        if k == 1:
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