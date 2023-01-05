def DFS(x, y):
    global cnt
    if x == n - 1 and y == n - 1:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < n and 0 <= yy < n and ch[xx][
                    yy] == 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())

board = [[0] * n for _ in range(n)]
ch = [[0] * n for _ in range(n)]
max = -2147000000
min = 2147000000
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] < min:
            min = tmp[j]
            sx = i
            sy = j
        if tmp[j] > max:
            max = tmp[j]
            ex = i
            ey = j
        board[i][j] = tmp[j]
ch[sx][sy] = 1
cnt = 0
DFS(0, 0)
print(cnt)

# 5
# 2 23 92 78 93
# 59 50 48 90 80
# 30 53 70 75 96
# 94 91 82 89 93
# 97 98 95 96 100
