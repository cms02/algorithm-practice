maze = [[0 for j in range(10)] for i in range(10)]
for i in range(10):
  maze[i] =  list(map(int,input().split()))

x=1
y=1
while True:
  if(maze[x][y] == 0):
    maze[x][y] = 9
  elif(maze[x][y] == 2):
    maze[x][y] = 9
    break

  if(maze[x][y+1] == 1 and maze[x+1][y] == 1 or (x==9 and y==9)):
    break

  if(maze[x][y+1] != 1):
    y += 1
  elif maze[x+1][y] != 1:
    x += 1


for i in range(10):
  for j in range(10):
    print(maze[i][j],end=' ')
  print()