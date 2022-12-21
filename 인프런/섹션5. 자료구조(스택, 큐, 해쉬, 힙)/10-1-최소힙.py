a = []
while True:
    k = int(input())
    if k == -1:
        break
    elif k == 0:
        print(a.pop(0))
    else:
        a.append(k)
        a.sort()
