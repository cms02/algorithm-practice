def DFS(L,sumS, sumT):
  global res
  if sumT > m:
    return
  if sumS > res:
    res = sumS
  else:
    return
  if sumT == m:
    return
  if sumT < m:
    for i in range(1, n+1):
      if ch[i] == 0:
        ch[i]=1
        DFS(L+1,sumS+slist[i],sumT+tlist[i])
        ch[i]=0



n, m = map(int, input().split())
slist = [0]*(n+1)
tlist = [0]*(n+1)
for i in range(1, n+1):
  s,t = map(int, input().split())
  slist[i] = s
  tlist[i] = t
  
ch = [0] * (n+1)
sum = 0
res = -21470000000
DFS(0,0,0)
print(res)




# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4