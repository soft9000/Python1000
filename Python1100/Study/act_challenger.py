
def show_banner(message = "Default Message"):
    print("*" * 5, message)


options = ("Show Banner", "Custom Banner", "Quit Program")


def show_menu():
    for ss, option in enumerate(options, 1):
        print(ss, ".)", option)


def get_choice():
    show_menu()
    return input("Input Number: ")


while True: # Loop forever!
    print()
    sel = get_choice()
    if sel == "1":
        show_banner()
        continue

    if sel == "2":
        show_banner(input("Input Message: "))
        continue

    if sel == "3":
        break

    show_banner("Bad number - try again!")

print("Program Ends.")
quit()




