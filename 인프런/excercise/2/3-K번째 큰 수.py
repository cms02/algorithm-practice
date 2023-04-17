n, k = map(int, input().split())
l = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            res.add(l[i] + l[j] + l[k])
res = list(res)
res.sort(reverse=True)
print(res[k - 1])
