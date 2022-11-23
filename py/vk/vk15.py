a = [0] * 9

for i in range(0, 10):
    if i < 9:
        a[i] = i + (i + 1) + (i + 2)

print(*a)
