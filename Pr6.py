# Project for senior citizen discount.
age=int(input("Enter you age:"))
if age>=60:
    print("You are eligible for senior citizen discount.")
else:
    print("You are not eligible for senior citizen discount, yet.")

# Project for leap year
cy=int(input("Enter the current year:"))
ystr=str(cy)
if ystr.endswith("00"):
    if cy%400==0:
        print("This year is a leap year.")
    else:
        print("This year is not a leap year.")
else:
    if cy%4==0:
        print("This year is a leap year.")
    else:
        print("This year is not a leap year.")

# Does it work?
# Yes it does!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!