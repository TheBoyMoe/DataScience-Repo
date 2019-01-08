ways = [3, 4, 5, 5, 4, 3]
p = 0
for n in ways:
    p += (n/36) * n/(n + 6)

p += (6/36) + (2/36)
print(p)
