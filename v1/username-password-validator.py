print("provide a username")
username = input()
if username.islower():
    print("username validation failed: all lowercase letters provided")
    exit()

if username.isupper():
    print("username validation failed: all uppercase letters provided")
    exit()

print("username is valid")

print("provide a password")
password = input()
if password.islower():
    print("password validation failed: all lowercase letters provided")
    exit()

if password.isupper():
    print("password validation failed: all uppercase letters provided")
    exit()

contains_special_character = False
for p in password:
    if p in "!#$%&":
        contains_special_character = True

if not contains_special_character:
    print("password validation failed: no special character letters provided")
    exit()

print("password is valid")