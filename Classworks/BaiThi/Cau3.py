# Cau3

def check_valid_email(word):
    if word.count("@") != 1:
        return False
    if not word.endswith("@gmail.com") and not word.endswith("@ymail.com"):
        return False
    return True

with open("Files/email.txt") as f:
    text = f.read()
    words = text.split()
    valid_emails = []
    for word in words:
        if check_valid_email(word):
            valid_emails.append(word)
            print(word)
    print("Trong văn bản vừa nhập có %i email" %len(valid_emails))