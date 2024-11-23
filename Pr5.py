# Project 23/11/24 C5
# Since divisibility rule of 6 is that the given number should be even and divisible by 3, we'll do it that way.
print("This is a program to check if a number is divisible by 6!")
num=int(input("Enter a number to see if it is divisible by 6:"))
a=num%2
if a==0 :
    b=True
else:
    b=False

a2=num%3

if a2==0:
    c=True
else:
    c=False

if b==True and c==True:
    print("Your number is divisible by 6!!!")
else:
    print("Your number is not divisible by 6...")    

# Thank you mam!