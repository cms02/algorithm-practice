n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for idx, val in enumerate(a):
  if val == m:
    print(idx+1)
    break
