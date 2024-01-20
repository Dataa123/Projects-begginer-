import random
while True:
    print("Welcome to the dice rolling simulator!")
    roll = input("Press enter to roll the dice: ")

    roll = ""
    num_rolls = 1
    roll_results = str(random.randint(1, 6)) 
    comp_result = str(random.randint(1, 6)) 
    for i in range(num_rolls):
        print("Your dice result is: " + roll_results)
        print("computer dice result is: " + comp_result)
    if int(roll_results) > int(comp_result):
        print("YOU WIN!!!")
    elif int(roll_results) == int(comp_result):
        print("Tie!!!")
    else:
        print("YOU LOST!!!")