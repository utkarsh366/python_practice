# Create a table of any no
# n = int (input ("enter a no"))

# for i in range (1, 11):
#     print (f"{n} X {i} = { n *i}")



# print name with letter "S"
# l = [" shubham", "Shrey", "Apple"]

# for name in l:
#     if (name.startswith("S")):
#         print(f"Hello { name}")

# 3. Do problem 1 with while loop

# # n = int (input ("enter a no"))

# i = 1

# while (i<11):
#     print (f"{n} X {i} = { n *i}")
#     i = i + 1


# 4. check if prime or not
# n = int (input ("enter a no"))

# for i in range (2, n/2):
#     if (n%i) == 0 :
#         print(f"{n} is not a prime no") 
#         break
# else:
#     print(f"{n} is a prime no")

# 5 fine th esum of first 10 natural no using while loop

# i = 0
# n = 0
# while (i< 10):
#     n = i + 1
#     i = i + 1

# print (n)

# 6. fqactorial of a given no with a for loop

# n = int(input ("Enter a no: "))
# product = 1
# for i in range(1, n+1):
#     product = product * i
# print(f"the factorial of product of {n} is {product}")

# 7. write a program to print a star pattern, n =3
#   *
#  ***
# *****
n=3
t = 3
for i in range (n, 1):
    for i in range (i,n-1):
        print("*")

    n= n-1

