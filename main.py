print("Welcome to Python Pizza!")
bill = 0
current_order = True

while current_order:
    size = input("What size pizza do you want? S,M or L?: ")
    add_pepperoni = input("Do you want pepperoni? Y or N: ")
    extra_cheese = input("Do you want extra cheese? Y or N: ")

    if size == 'S':
        bill += 15
    elif size == 'M':
        bill += 20
    elif size == 'L':
        bill += 25

    if add_pepperoni == 'Y':
        if size == 'S':
            bill += 2
        else:
            bill += 3

    if extra_cheese == 'Y':
        bill += 1

    response = input("Do you want to add someone else? Y or N: ")
    if response == 'Y':
        current_order = True
    else:
        current_order = False

print(f"Your total bill is ${bill}")

