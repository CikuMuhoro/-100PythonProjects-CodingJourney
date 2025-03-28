def capitalizing():
    str1 = input("enter a string with atlest four characters : ")
    if len(str1) < 4:
        print("Please enter atleast four charcters")
        return

    for i, char in enumerate(str1):
        if i == 0 or i == 3:
            print(char.upper(), end="")
        else:
            print(char, end="")


capitalizing()
