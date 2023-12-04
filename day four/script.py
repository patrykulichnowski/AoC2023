f = open("C:/Users/Patryk/Desktop/python/day four/data.txt", "r")
res = 0
for line in f:
    line = line.strip()
    data = line.split(": ")[1]
    card = data.split(" | ")[0].split()
    winningNumbers = data.split(" | ")[1].split()

    points = 0
    for n in card:
        for m in winningNumbers:
            if n == m:
                if points == 0:
                    points += 1
                else:
                    points *= 2
    res += points
print(res)
f.close()
