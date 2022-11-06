# Cau2

def check_has_special_character(password):
    special_charater = "@#$*&"
    for character in special_charater:
        if password.count(character) > 0:
            return True
    return False

def check_has_number(password):
    for character in password:
        if character.isdigit():
            return True
    return False

def check_has_valid_character(password):
    valid_character = "abcdefghijklmnopqrstuvwxyz0123456789@#$*&"
    for character in password:
        if valid_character.count(character.lower()) <= 0:
            return False
    return True

def check_has_valid_uppercase(password):
    valid_character = "abcdefghijklmnopqrstuvwxyz".upper()
    for character in password:
        if valid_character.count(character) > 0:
            return True
    return False

def check_valid_password(password):
    if len(password) >= 8 and len(password) <= 20 \
            and check_has_special_character(password) \
            and check_has_number(password) \
            and check_has_valid_character(password) \
            and check_has_valid_uppercase(password):
        return True
    return False

while True:
    password = input("Enter you password: ")
    valid = check_valid_password(password)
    if valid:
        print(password, "là password hợp lệ")
        break
    else:
        print(password, "là password không hợp lệ")
