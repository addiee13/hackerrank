year = int(input("Enter a year: "))
def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            year = False
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    else:
        leap = False
    return leap
print(is_leap(year))
