import random
characters = []
validSymbols = "!%&*^(`)"

# adds the numbers into list of possible characters
for i in range(48, 58):
    characters.append(chr(i))

# adds the uppercase letters into list of possible characters
for i in range(65, 90):
    characters.append(chr(i))

# adds the lowercase letters into list of possible characters
for i in range(97, 123):
    characters.append(chr(i))

# appends the valid symbols into list of possible characters
for i in range(len(validSymbols)):
    characters.append(validSymbols[i])

count = int(input("How many turns would you like: "))

for i in range(count):
    password_length = int(input("How many characters would you like your password to be: "))
    password_amount = int(input("How many passwords would you like: "))
    for j in range(password_amount):
        secret_password = ""
        for k in range(password_length):
            password_char = random.choice(characters)
            secret_password += password_char
        print("This is your secret password: ", secret_password)