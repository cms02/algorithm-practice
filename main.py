n, m = map(int, input().split())
dy = [0] * (m + 1)
for i in range(n):
    w, v = map(int, input().split())
    for j in range(w, m + 1):
        dy[j] = max(dy[j], dy[j - w] + v)
print(dy[m])

# 4 11
# 5 12
# 3 8
# 6 14
# 4 8