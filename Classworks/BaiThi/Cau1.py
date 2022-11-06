# Cau1

def format_content(content):
    special_characters = [";", ".", ",", "-", "–"]
    for character in special_characters:
        while character in content:
            content = content.replace(character, "")
    return content

with open("Files/baitho.txt") as f:
    baitho = f.read()
    formatted_baitho = format_content(baitho)
    count_dict = {}
    words = formatted_baitho.split()
    for word in words:
        count = words.count(word)
        count_dict[word] = count
    print(count_dict)
