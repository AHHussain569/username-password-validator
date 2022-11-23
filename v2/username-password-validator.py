from validators import lowercase_validator, uppercase_validator, special_char_validator


def validate(text, text_validators):
    for validator in text_validators:
        invalid = validator(text)
        if invalid:
            return invalid

    return ""


print("provide a username")
username = input()
username_validators = [lowercase_validator, uppercase_validator]
username_invalid = validate(username, username_validators)
if username_invalid:
    print("username validation failed:", username_invalid)
    exit()
print("username is valid")

print("provide a password")
password = input()
password_validators = [lowercase_validator, uppercase_validator, special_char_validator]
password_invalid = validate(password, password_validators)
if password_invalid:
    print("password validation failed:", password_invalid)
    exit()
print("password is valid")