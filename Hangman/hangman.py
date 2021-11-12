import random
print("HANGMAN")
print("The game will be available soon.")

word_list = ['python', 'java', 'javascript', 'php']
secrets = random.choice(word_list)
x = input("Guess the word:")
print(x)
if x in secrets:
    print("You survived!")
else:
    print("You lost!")



# secret = random.choice(word_list)
# str_word = str(input())
# guesse = input("Guess the word:" + str_word)
# if guesse in secret:
#     print("You survived!")
# else:
#     if guesse not in secret:
#         print("You lost!")

