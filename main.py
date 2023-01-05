def DFS(L,s):
  global res
  if L==m:
    for x in cb:
      print(x, end=' ')
    print()
  else:
    for i in range(s, len(pz)):
      cb[L] = i
      DFS(L+1, i+1)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
hs = []
pz = []
cb = [0] * m
res = 2147000000
for i in range(n):
  for j in range(n):
    if board[i][j] == 1:
      hs.append((i,j))
    elif board[i][j] == 2:
      pz.append((i,j))
DFS(0,0)