                # 1. display user name using input

# userName = input("Enter user name:")

# print ("Usern name is", userName)
# print (f"Good afternoon {userName}, Today is very nice day")

                # 2. write a program to  fill in a letter tempelate given below with name and date 
                #letter template '''
                #Dear [name],
                #I am writing to inform you that your [adjective] [noun] has been received.
                #The [adjective] [noun] was received on [date] and is currently being processed
                #Sincerely,
                #[Your Name]
                #'''

# letter = '''
# Dear [name],
# I am writing to inform you that your [adjective] [noun] has been received.
# The [adjective] [noun] was received on [date] and is currently being processed
# Sincerely,
# [Your Name]'''

# letter = letter.replace("[name]", "utkarsh").replace("[date]", "7-july")

# print(letter)

                # 3. Write a program to detect double space in string

# s = "hello  String"
# print(s.count("  ")) # count double space in string

                # 4. Replace double space with single space
# s = " hello string"

# s = s.replace("  ", " ")
# print(s) # replace double space with single space in string

# 5. write a program to format the following letter using escape equence character

#letter = "dear utkarsh, this practice work is nice, Thank you!"
letter = "Dear utkarsh,\nThis practice work is nice, Thank you!"
print(letter)





