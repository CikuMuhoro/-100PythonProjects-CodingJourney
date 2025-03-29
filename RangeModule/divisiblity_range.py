def divisiblity_range():
    result = []
    for numbertest in range(2000, 3201, 1):

        if numbertest % 7 == 0 and numbertest % 5 != 0:
            result.append(str(numbertest))
    print(", ".join(result))


divisiblity_range()
