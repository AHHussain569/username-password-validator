def lowercase_validator(text):
    return "all lowercase letters provided" if text.islower() else ""


def uppercase_validator(text):
    return "all uppercase letters provided" if text.isupper() else ""


valid_special_chars = "!#$%&"


def special_char_validator(text):
    for p in text:
        if p in valid_special_chars:
            return ""
    return "no special characters provided"
