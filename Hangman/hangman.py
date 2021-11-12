import random
print("HANGMAN")
print("The game will be available soon.")


# word = ["python"]
# x = input("Guess the word:")
# print(x)
# if x in word:
#     print("You survived!")
# else:
#     print("You lost!")
#
#
# word_list = ['python', 'java', 'javascript', 'php']
# secrets = random.choice(word_list)
# x = input("Guess the word:")
# print(x)
# if x in secrets:
#     print("You survived!")
# else:
#     print("You lost!")


word_list = ['python', 'java', 'javascript', 'php']
secrets = random.choice(word_list)

len_secrets = len(secrets[2:-1])
print(secrets[:3] + '-'*len_secrets)
x = input("Guess the word:")
print(x)
if x == secrets:
    print("You WON")
else:
    print("You lost!")


