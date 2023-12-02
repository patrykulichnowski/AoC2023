# only 12 red cubes, 13 green cubes, and 14 blue cubes
file = open("C:/Users/Patryk/Desktop/adc2023/day two/data.txt", "r")
res = 0
maxR = 12
maxG = 13
maxB = 14
for line in file:
    possible=True
    indexOfGame = line.split(":")[0]
    indexOfGame = indexOfGame[5:]
    game = line.split(": ")[1]
    game = game.strip().split("; ")
    for blocks in game:
        blocks = blocks.split(", ")
        for move in blocks:
            move = move.split(" ")
            if move[1] == "blue":
                if int(move[0]) > maxB:
                    possible = False
            elif move[1] == "red":
                if int(move[0]) > maxR:
                    possible = False
            elif move[1] == "green":
                if int(move[0]) > maxG:
                    possible = False
    if possible:
        res += int(indexOfGame)
print(res)
file.close()