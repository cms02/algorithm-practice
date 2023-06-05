a = input()
b = input()

sH = dict()

for i in a:
  sH[i] = sH.get(i, 0) + 1

for i in b:
  sH[i] = sH.get(i, 0) - 1
for i in a:
    if sH.get(i) > 0:
        print("NO")
        break
else:
    print("YES")