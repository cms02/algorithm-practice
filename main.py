def DFS(index, value):
  if value > c:
    return
  if index == n:
    if value >= max:
      max = value
  else:
    DFS(index+1, value)
    DFS(index+1, value + a[index])
    
c, n = map(int,input().split())
a = []
max = -1
for _ in range(n):
  a.append(int(input()))
DFS(0,0)
