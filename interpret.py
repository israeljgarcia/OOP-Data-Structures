#file_path = input("Enter file: ")
pythonref = open('text.py', "r")
csharpref = open('csharp.cs', 'w')

for line in pythonref:
    csharp_line = []
    words = line.split()
    for word in words:
        if word == 'class':
            csharp_line.append(word)
            csharp_line.append(words[1])
            csharp_line.append(' {')

pythonref.close()
csharpref.close()
