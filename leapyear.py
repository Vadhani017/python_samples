# to check whether the given year is leap year or not

def leap_year(given_year):
    """
Not every year divided by 4 are leap year.
For example, consider 2100, it is not leap year.
So, here is the following program, to find out leap year.
    """
    if given_year % 4 == 0:
        if given_year % 100 == 0:
            if given_year % 400 == 0:
                print("It is a leap year")
            else:
                print("It is not a leap year")
        else:
            print("It is a leap year")


year = int(input("Enter the year: "))
leap_year(year)
