
file = open("C:/Users/Patryk/Desktop/adc2023/day two/data.txt", "r")
res = 0
for line in file:
    indexOfGame = line.split(":")[0]
    indexOfGame = indexOfGame[5:]
    game = line.split(": ")[1]
    game = game.strip().split("; ")
    maxR = 0
    maxG = 0
    maxB = 0
    for blocks in game:
        blocks = blocks.split(", ")
        for move in blocks:
            move = move.split(" ")
            if move[1] == "blue":
                if int(move[0]) > maxB:
                    maxB = int(move[0])
            elif move[1] == "red":
                if int(move[0]) > maxR:
                    maxR = int(move[0])
            elif move[1] == "green":
                if int(move[0]) > maxG:
                    maxG = int(move[0])
    res += maxG * maxB * maxR
print(res)
file.close()