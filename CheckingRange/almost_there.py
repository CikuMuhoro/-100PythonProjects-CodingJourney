def almost_there():
    a = int(input("Enter an integer within 10 of either 100 or 200:"))

    if (a >= 90 and a <= 110) or (a >= 190 and a <= 210):
        print("True")
    else:
        print("false")


almost_there()
