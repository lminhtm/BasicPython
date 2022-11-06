# Cau4

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
    while "  " in string:
        string = string.replace("  ", " ")
    string = string.replace("\n ", "\n")
    string = string.replace("\t", "")
    return string

content = read_text_file("Files/Quehuong.txt")
print("Bài thơ trước khi được định dạng\n%s" %("*"*40))
print(content)
print("Bài thơ sau khi được định dạng\n%s" %("*"*40))
print(formatted_string(content))
