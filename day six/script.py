f = open("C:/Users/Patryk/Desktop/adc2023/day six/data.txt", "r")
data = f.readlines()
time = data[0].strip()
distance = data[1].strip()
time = time.split()
distance = distance.split()
time.pop(0)
distance.pop(0)
res = 1
for i in range(0, len(time)):
    maxTime = int(time[i])
    maxDistance = int(distance[i])
    counter = 0
    for j in range(0, int(time[i]) + 1):
        d = maxTime * j
        if d > maxDistance:
            counter += 1
        maxTime -= 1
    res *= counter
print(res)
f.close()