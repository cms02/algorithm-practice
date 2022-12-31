def DFS(L, sumT, sumP):
    global res
    if sumT > n:
        return
    if sumP > res:
        res = sumP
    else:
        return
    if sumT <= n:
        for i in range(sumT, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                DFS(L + 1, sumT + tlist[i], sumP + plist[i])
                ch[i] = 0


n = int(input())
tlist = [0] * (n + 1)
plist = [0] * (n + 1)

for i in range(1, n + 1):
    t, p = map(int, input().split())
    tlist[i] = t
    plist[i] = p

res = -2147000000
ch = [0] * (n + 1)
d = []
DFS(0, 0, 0)
print(res)

# 7
# 4 20
# 2 10
# 3 15
# 3 20
# 2 30
# 2 20
# 1 10
