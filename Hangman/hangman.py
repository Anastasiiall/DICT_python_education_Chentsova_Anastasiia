print("HANGMAN")
print("The game will be available soon.")

words_list = ['python,java']
secret = random.choice(words_list)
print("Guess the word:")
def Hangman(words):
    words = str(input())
    if str(input()) in secret
    print("You survived!")
else:
    if str(input()) not in secret
    print("You lost!")


word_list = ['python', 'java', 'javascript', 'php']

import random

secret = random.choice(word_list)
str_word = str(input())
guesse = input("Guess the word:" + str_word)
if guesse in secret:
    print("You survived!")
else:
    if guesse not in secret:
        print("You lost!")
