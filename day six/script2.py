#it runs like shit
f = open("C:/Users/Patryk/Desktop/adc2023/day six/data.txt", "r")
data = f.readlines()
time = data[0].strip()
distance = data[1].strip()
time = time.split()
distance = distance.split()
time.pop(0)
distance.pop(0)
res = 0
t = ''
d = ''
for i in time:
    t += i
for i in distance:
    d += i
tt = int(t)
for i in range(0, int(t) + 1):
    if i * tt > int(d):
        res += 1
    tt -= 1
print(res)
f.close()