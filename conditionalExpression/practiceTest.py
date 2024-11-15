# 1. find the greatest of 4 no entered by user
# Input numbers from the user
a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
c = int(input("Enter no 3: "))
d = int(input("Enter no 4: "))

# Find the greatest number
if (a > b) and (a > c) and (a > d):
    print("The greatest number is:", a)
elif (b > a) and (b > c) and (b > d):
    print("The greatest number is:", b)
elif (c > a) and (c > b) and (c > d):
    print("The greatest number is:", c)
else:
    print("The greatest number is:", d)
