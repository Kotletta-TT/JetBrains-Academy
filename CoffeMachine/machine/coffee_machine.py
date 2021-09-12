resource = [120, 400, 540, 9]
money = 550
cappuccino = [12, 200, 100, 1]
latte = [20, 350, 75, 1]
espresso = [16, 250, 0, 1]
chose_coffee = [cappuccino, latte, espresso]

def check_resource(chose_coffee):
    index = 0
    for item in chose_coffee:
        if resource[index] - item >= 0:
            index += 1
        else:
            print("I have enough resources, making you a coffee!")
            return False
    return True

def commit_buy(chose_coffee, price):
    global resource, money
    index = 0
    for item in chose_coffee:
        resource[index] -= item
        index += 1
    money += price


def status():
    print(f"""The coffee machine has:
          {resource[1]} of water
          {resource[2]} of milk
          {resource[0]} of coffee beans
          {resource[3]} of disposable cups
          {money} of money""")

def buy():
    global resource, money
    chose_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino back - to main menu:\n")
    if chose_coffee == "1":
        if check_resource(espresso):
            commit_buy(espresso, 4)
    elif chose_coffee == "2":
        if check_resource(latte):
            commit_buy(latte, 7)
    elif chose_coffee == "3":
        if check_resource(cappuccino):
            commit_buy(cappuccino, 6)
    elif chose_coffee == "back":
        return

def fill():
    resource[1] += int(input("Write how many ml of water do you want to add:\n"))
    resource[2] += int(input("Write how many ml of milk do you want to add:\n"))
    resource[0] += int(input("Write how many grams of coffee beans do you want to add:\n"))
    resource[3] += int(input("Write how many disposable cups of coffee do you want to add:\n"))

def take():
    global money
    print(f"I gave you ${money}\n")
    money = 0

def start():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        if action == "buy":
            buy()
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "remaining":
            status()
        elif action == "exit":
            exit()
        else:
            print("Please correct input\n")

start()

# ###################################TWO PART#############################################
# supply_water = int(input("Write how many ml of water the coffee machine has:\n"))
# supply_milk = int(input("Write how many ml of milk the coffee machine has:\n"))
# supply_coffee = int(input("Write how many grams of coffee the coffee machine has:\n"))
# need_cups = int(input("rite how many cups of coffee you will need:\n"))
#
# amount_cups = min(supply_coffee // COFFEE_CUP, supply_milk // MILK_CUP,
#                   supply_water // WATER_CUP)
#
# if amount_cups == need_cups:
#     print("Yes, I can make that amount of coffee")
# elif amount_cups > need_cups:
#     diff = amount_cups - need_cups
#     print(f"Yes, I can make that amount of coffee (and even {diff} more than that)")
# else:
#     print(f"No, I can make only {amount_cups} cups of coffee")
# #####################################FIRST PART########################################
# print("Write how many cups of coffee you will need:")
# count_coffee = abs(int(input()))
# print(f"For {count_coffee} cups of coffee you will need:")
# print(f"{count_coffee * WATER_CUP} ml of water")
# print(f"{count_coffee * MILK_CUP} ml of milk")
# print(f"{count_coffee * COFFEE_CUP} g of coffee beans")