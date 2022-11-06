# Cau2

def check_valid_password(password):
    # Length
    if len(password) < 8 or len(password) > 20:
        return False

    # Prepare
    special_charater = "@#$*&"
    valid_character = "abcdefghijklmnopqrstuvwxyz0123456789@#$*&"
    valid_az_character = "abcdefghijklmnopqrstuvwxyz"

    # Special character
    has_special_character = False
    for character in special_charater:
        if password.count(character) > 0:
            has_special_character = True
            break
    if has_special_character == False:
        return False

    # Number
    has_number = False
    for character in password:
        if character.isdigit():
            has_number = True
            break
    if has_number == False:
        return False

    # a-z, A-Z
    has_valid_character = True
    has_valid_uppercase_character = False
    for character in password:
        if valid_character.count(character.lower()) <= 0:
            has_valid_character = False
            break
        if valid_az_character.upper().count(character) > 0:
            has_valid_uppercase_character = True
    if has_valid_character == False or has_valid_uppercase_character == False:
        return False

    return True

while True:
    password = input("Enter you password: ")
    valid = check_valid_password(password)
    if valid:
        print(password, "là password hợp lệ")
        break
    else:
        print(password, "là password không hợp lệ")