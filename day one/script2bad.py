file = open("C:/Users/Patryk/Desktop/adc2023/1/data.txt", "r")
result = 0
for line in file:
    firstFound = 0
    lastFound = 0
    numberInLine = 0
    #problem taki ze to znajduje tylko pierwszy index jak jest np ninegfs2nine to zwroci mi liczbe 92 zamiast 99
    indexes = [
        line.find("one"),
        line.find("two"),
        line.find("three"),
        line.find("four"),
        line.find("five"),
        line.find("six"),
        line.find("seven"),
        line.find("eight"),
        line.find("nine")
        ]
    
    for i in range(0,len(line.strip())):
        if ord(line[i]) < 97:
            if(firstFound == 0):
                firstFound = line[i]
                indexOfFirstDigit = i
            lastFound = line[i]
            indexOfLastDigit = i

    for i in range(0, len(indexes)):
        if (indexes[i] >= 0 and indexes[i] <= indexOfFirstDigit):
            firstFound = i + 1
            indexOfFirstDigit = indexes[i]
        elif indexes[i] >= indexOfLastDigit:
            lastFound = i + 1
            indexOfLastDigit = indexes[i]

    numberInLine = str(firstFound) + str(lastFound)
    result = result + int(numberInLine)
    print(line.strip())
    print(numberInLine)
    # print(str(indexOfFirstDigit) + " " + str(indexOfLastDigit))
    # print(indexes)

print(result)
file.close()