file_path = input("Enter file: ")
fileref = open(file_path, "r")
words = 0
lines = 0

for aline in fileref:
    words += len(aline.split())
    lines += 1

print(f'The file contains {lines} lines and {words} words.')
fileref.close()