#
# Made By Savan
#

# This Function Is used to check the strength of a user entered password
def password_strength(password):
    # Some rules for strong password
    rules = [
        len(password) >= 8,
        any(char.islower() for char in password),
        any(char.isupper() for char in password),
        any(char.isdigit() for char in password),
        any(char in "!@#$%^&*()-_+=" for char in password)
    ]

    # Count of passed rules
    strength = sum(rules)

    # provides feedback
    if strength == 5:
        print("Strong password")
    elif strength >= 3:
        print("Medium Password")
    else:
        print("Weak password")

# Displaying rules to user
print("--Rules For Creating Strong Password-- \n1. Password Length Should Be 8. \n2. Password Must Have Lower & Upper Letters. \n3. It Must Contain Digits & Special Symbols.\n")

# user input for a password
user_password = input("Enter a password: ")

# Displays the strength of the password
password_strength(user_password)
print("Password Strength:")
