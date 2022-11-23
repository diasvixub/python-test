a = [0] * 10
n = 0

for i in range(-10, 10, 2):
    a[n] = i
    n += 1

print(*a)
