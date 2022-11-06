# Cau4

def formatted_content(content):
    while "  " in content:
        content = content.replace("  ", " ")
    content = content.replace("\n ", "\n")
    content = content.replace("\t", "")
    return content

f = open("Files/Quehuong.txt")
content = f.read()
print("Bài thơ trước khi được định dạng\n%s" %("*"*40))
print(content)
print("Bài thơ sau khi được định dạng\n%s" %("*"*40))
print(formatted_content(content))
f.close()