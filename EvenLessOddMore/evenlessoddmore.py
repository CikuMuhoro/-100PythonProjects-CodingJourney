def user_input():
    try:
        a = int(input("Enter two numbers.\n Enter first number:"))
        b = int(input("Enter second number:"))

        if a % 2 == 0 and b % 2 == 0:
            small = min(a, b)
            print(f"both are even, and smaller number is:{small}")
        else:
            big = max(a, b)
            print(f"you entered an odd number, and bigger numer is:{big}")

        return f"Nuber you entered were: {a} and {b}"

    except ValueError:
        return "only numbers are expected."


print(user_input())
