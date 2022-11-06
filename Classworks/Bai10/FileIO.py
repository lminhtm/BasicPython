"""
Bai10. FILE IO
"""

# Open
"""
r: open for reading (default)
w: open for writing, truncating the file first
x: open for exclusive creation, failing if the file already exists
a: open for writing, appending to the end of file if it exists
b: binary mode
t: text mode (default)
+: open for updating (reading and writing)
"""
f = open("Files/bai_tho.txt", "r")
content = f.read()
print(content)
f.close()

# Write
fa = open("Files/file1.txt", "w+")
fa.write("Hello world")
fa.close()

# Read
f = open("Files/bai_tho.txt", "r+")
content = f.read(12)
print("\n12 bytes content:", content)
f.close()

# Check pos
f = open("Files/bai_tho.txt", "rb+")
pos = f.tell()
print("File current position:", pos)

# Seek
pos = f.seek(5, 0) # Seek 5 byte from the beginning of file
pos = f.seek(-20, 2) # Seek 20 bytes back from the end of file
pos = f.seek(5, 1) # Seek 5 bytes from current position
print("12 bytes content after seek to beginning:", f.read(12))
f.close()
