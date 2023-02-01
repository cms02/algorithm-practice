n, m = map(int, input().split())
dy = [0] * (m+1)
for i in range(n):
  ps, pt = map(int, input().split())
  for j in range(m, pt-1, -1):
    dy[j] = max(dy[j], dy[j-pt] + ps)
print(dy[m])

# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4