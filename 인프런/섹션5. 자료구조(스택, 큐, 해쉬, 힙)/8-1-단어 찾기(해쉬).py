n = int(input())
a = []
used = []
for _ in range(n):
    a.append(input())

for _ in range(n - 1):
    used.append(input())

while a:
    w = a.pop()
    if w in used:
        continue
    else:
        print(w)
        break
