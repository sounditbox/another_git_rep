l = r = 0
with open('data.txt', 'r') as f:
    for line in f:
        x, y = line.split()
        l += int(x)
        r += int(y)
print(l - r)
