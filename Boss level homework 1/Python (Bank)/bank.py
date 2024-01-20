#Greeting

print("Welcome to GOA Bank!")
print("First, complete the registration please.")

#Registration form
name = input("Enter your full name: ")
print("Information saved! Your name is:", name)
email = input("Enter your email: ")
print("Information saved! Your mail is:", email)
date = input("Enter your birth day, month and year: ")
print("Information saved! Your date of birth is:", date)

if name == "" or email == "" or date == "":
    print("Registration wasn't complete! Try again.")
else:
    print("Registration was complete!")
    print("Account created succesfully!")

    #Account data

    balance = 0

    print("Your current data:")
    print("Balance:", balance)

    #Transfering money

    print("Transfer money in your account here:")
    money = input("Enter money you want to transfer: ")
    print(money, "dollar transfered in your account.")
    print("Balance:", balance + int(money))
    
    #Created new balance variable

    balance += int(money)

    #Taking money

    print("Take money from account from here:")
    take_money = input("Enter money you want to take: ")

    if int(take_money) > balance:
        print("You have not got that much money on your balance, your balance is:", balance)
        take_money = input("Enter money you want to take: ")
        print("You took", take_money, "dollar from your account.")
        print("Balance:", balance - int(take_money))
    else:
        print("You took", take_money, "dollar from your account.")
        print("Balance:", balance - int(take_money))