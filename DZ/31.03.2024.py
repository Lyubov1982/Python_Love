file = "dz.txt"

f = open(file, "w")
f.write("Замена строки в текстовом файле:\nизменить строку в списке;\nзаписать список в файл;\n")
f.close()
#
f = open(file, "r+")
lines = f.readlines()
lines[1], lines[2] = lines[2], lines[1]
f.seek(0)
for line in lines:
    f.write(line)
f.close()
#
f = open(file, "r")
lines = f.readlines()
f.close()
print(lines)

