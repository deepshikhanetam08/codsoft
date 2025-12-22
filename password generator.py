import random
import string
caps = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
digits = list(string.digits)
special = ['_','&','@','!','#','*','(',')']
allvariable = caps + digits + special + lower 

password = ""

length = int(input("Length of Password:"))

for i in range(length):
    password += random.choice(allvariable)

print("The Generated Password is:", password)

