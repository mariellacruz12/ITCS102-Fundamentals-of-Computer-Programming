#boolean variable
flood_control = True

while flood_control == True:
    ask = input("Do you want to continue? (yes/no) ----> ")

    if ask.lower() == "yes":
        print("Continuing the program...")
        continue
    else:
        print("Exiting the program...")
        break