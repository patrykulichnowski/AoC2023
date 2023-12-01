file = open("C:/Users/Patryk/Desktop/adc2023/1/data.txt", "r")
result = 0
for line in file:
    digits = []
    for i, character in enumerate(line.strip()):
        if character.isdigit():
            digits.append(character)
        for value, stringN in enumerate([
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine"
        ]):
            if line[i:].startswith(stringN):
                digits.append(str(value+1))
    lineNumber = int(digits[0]+digits[-1])
    result += lineNumber
print(result)
file.close()