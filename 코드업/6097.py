h, w = map(int, input().split())

zeros = []
# for i in range(h+1):
#   zeros.append([])
#   for j in range(w+1):
#     zeros[i].append(0)

zeros = [[0] * w for _ in range(h)]

n = int(input())

  
for i in range(n):
  l,d,x,y = map(int, input().split())
  for j in range(l):
    if(d==0):
      zeros[x-1][y-1+j] = 1
    else:
      zeros[x-1+j][y-1] = 1

for i in range(h):
  for j in range(w):
    print(zeros[i][j], end=' ')
  print()
    
    
      
  
