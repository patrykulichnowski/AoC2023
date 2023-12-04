fname = 'C:/Users/Patryk/Desktop/python/day four/test.txt'
with open(fname, 'r') as f:
    last_line = f.readlines()[-1]
maxCard = last_line.split(":")[0]
maxCard = int(maxCard[5:])
# above is to get the last number of the scratchcard, that will be needed below in few functions

f = open(fname, "r")
i = 0
scratchCardsAmount = []

for j in range(0, maxCard):
    scratchCardsAmount.append(1)

for line in f:
    line = line.strip()
    data = line.split(": ")[1]
    card = data.split(" | ")[0].split()
    winningNumbers = data.split(" | ")[1].split()

    for re in range(scratchCardsAmount[i]):
        points = 0
        for n in card:
            for m in winningNumbers:
                if n == m:
                    points += 1
        # print(i+1)
        # print(i+points)
        # print("step")
        for j in range(i+1, i + points):
            if j < maxCard:
                scratchCardsAmount[j] += 1
    i += 1
res = 0
print(scratchCardsAmount)
for x in scratchCardsAmount:
    res += x

print(res)
f.close()
