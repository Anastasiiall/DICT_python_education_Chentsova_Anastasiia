import random


def first():
    dengi = [round(( money / kolvo), 2)] * kolvo
    for i in range(len(spisok)):
        dict[spisok[i]] = dengi[i]
    print("No one is going to be lucky :( ")
    print(dict)


def second():
    if kolvo == 1:
        print("This is Impossible!")
        first()
    elif kolvo > 1:
        dengi = [round(( money / (kolvo - 1)), 1)] * kolvo
        jack_1 = random.choice(range(kolvo))
        jack = random.choice(range(kolvo))
        for i in range(len(spisok)):
            dict[spisok[i]] = dengi[i]
            dict[spisok[jack_1]] = 0
        print(f"{spisok[jack]} is a lucky one!")
        print(dict)


while True:
    while True:
        try:
            kolvo = int(input("Enter the number of friends (including you): "))
            break
        except:
            print("Please enter only numbers!")
    if kolvo > 0:
        print("Enter the name of every friend (including you), each on a new line: ")
        names = [input() for i in range(kolvo)]
        dict = {names[x - 1]: 0 for x in range(1, kolvo + 1)}
        money = int(input("Enter the total amount: "))
        if int(money / kolvo) != (money / kolvo):
            list_name = [round((money / kolvo), 2)] * kolvo
        else:
            list_name = [round(money / kolvo)] * kolvo
        spisok = list(dict.keys())
        spisok.sort()
        lucky = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No: ")
        if lucky == "Yes":
            second()
            break
        elif lucky == "No":
            first()
            break
        break
    elif kolvo < 0:
        print("It Impossible")
        continue
    else:
        print("No one is join for the party.")
        break
