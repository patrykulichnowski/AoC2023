file = open("C:/Users/Patryk/Desktop/adc2023/1/data.txt", "r")
result = 0
for line in file:
    first = 0
    last = 0
    x = 0
    for character in line.strip():
        if ord(character) < 97:
            if(first == 0):
                first = character
            last = character
    x = first + last
    result += int(x)
print(result)
file.close()