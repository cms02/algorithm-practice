N = int(input())
count = 0
for i in range(2, N + 1):
    for j in range(2, i):
        if (i % j) == 0:
            break
    else:
        count = count + 1
print(count)
