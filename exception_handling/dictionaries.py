file_path = 'census.csv'
fileref = open(file_path, "r")
lines = 0

education_level = {}

for aline in fileref:
    words = aline.split(',')

    level = words[3]

    if level not in education_level:
        count = 1
        education_level[level] = count

    if level in education_level:
        education_level[level] += 1

fileref.close()

for key in education_level:
    print(f'{education_level[key]} -- {key}')
