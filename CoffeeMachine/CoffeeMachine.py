print("""
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
""")


def coffee_buy(water, milk, coffee_beans, disposable_cups, money):
    coffee = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: '))
    water_espresso = 250
    coffee_beans_espresso = 16
    money_espresso = 4
    water_latte = 350
    milk_latte = 75
    coffee_beans_latte = 20
    money_latte = 7
    water_cappuccino = 200
    milk_cappuccino = 100
    coffee_beans_cappuccino = 12
    money_cappuccino = 6
    if coffee == '1':
        water -= water_espresso
        coffee_beans -= coffee_beans_espresso
        disposable_cups -= 1
        money += money_espresso
    elif coffee == '2':
        water -= water_latte
        milk -= milk_latte
        coffee_beans -= coffee_beans_latte
        disposable_cups -= 1
        money += money_latte
    else:
        water -= water_cappuccino
        milk -= milk_cappuccino
        coffee_beans -= coffee_beans_cappuccino
        disposable_cups -= 1
        money += money_cappuccino
    print('The coffee machine has:')
    print('%d of water' % water)
    print('%d of milk' % milk)
    print('%d of coffee_beans' % coffee_beans)
    print('%d of disposable cups' % disposable_cups)
    print('%d of money' % money)


def coffee_fill(water, milk, coffee_beans, disposable_cups):
    water_fill = int(input('Write how many ml of water do you want to add: '))
    milk_fill = int(input('Write how many ml of milk do you want to add: '))
    coffee_beans_fill = int(input('Write how many grams of coffee beans do you want to add: '))
    disposable_cups_fill = int(input('Write how many disposable cups of coffee do you want to add: '))
    water += water_fill
    milk += milk_fill
    coffee_beans += coffee_beans_fill
    disposable_cups += disposable_cups_fill
    print('The coffee machine has:')
    print('%d of water' % water)
    print('%d of milk' % milk)
    print('%d of coffee_beans' % coffee_beans)
    print('%d of disposable cups' % disposable_cups)
    print('%d of money' % money)


def coffee_money(money):
    print('I gave you $%d' % money)
    money = 0
    print()
    print('The coffee machine has:')
    print('%d of water' % water)
    print('%d of milk' % milk)
    print('%d of coffee_beans' % coffee_beans)
    print('%d of disposable cups' % disposable_cups)
    print('%d of money' % money)

water = 1200
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550
print('The coffee machine has:')
print('%d of water' % water)
print('%d of milk' % milk)
print('%d of coffee_beans' % coffee_beans)
print('%d of disposable cups' % disposable_cups)
print('%d of money' % money)
action = input('Write action (buy, fill, take): ')
if action == 'buy':
    coffee_buy(water, milk, coffee_beans, disposable_cups, money)
elif action == 'fill':
    coffee_fill(water, milk, coffee_beans, disposable_cups)
else:
    coffee_money(money)

