# Cau1

def read_text_file(file_name):
    content = ""
    try:
        f = open(file_name)
        content = f.read()
    except UnicodeDecodeError as err:
        try:
            a = open(file_name, encoding="utf-8")
            content = a.read()
        except:
            print("Read error")
        finally:
            a.close()
    except:
        print("Read error")
    finally:
        f.close()
        return content

def formatted_string(string):
    special_characters = [";", ".", ",", "-", "–"]
    for character in special_characters:
        while character in string:
            string = string.replace(character, "")
    return string

baitho = read_text_file("Files/baitho.txt")
words = formatted_string(baitho).split()
count_dict = {}
for word in words:
    count = words.count(word)
    count_dict[word] = count
print(count_dict)
