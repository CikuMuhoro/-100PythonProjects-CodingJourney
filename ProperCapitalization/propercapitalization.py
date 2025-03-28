def noun_test():

    try:
        str1, str2 = input("Enter your first name and last name :").split()

        if str1[0].isupper() and str2[0].isupper():
            print("True")
        else:
            print("False")

    except ValueError:
        print("A name should always start with capital letters")


noun_test()
