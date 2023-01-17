n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

dy = [[0] * (n) for _ in range(n)]

dy[0][0] = board[0][0]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        if i == 0:
            dy[i][j] = dy[i][j - 1] + board[i][j]
        elif j == 0:
            dy[i][j] = dy[i - 1][j] + board[i][j]
        else:
            dy[i][j] = min(dy[i - 1][j], dy[i][j - 1]) + board[i][j]
print(dy[n - 1][n - 1])

# 5
# 3 7 2 1 9
# 5 8 3 9 2
# 5 3 1 2 3
# 5 4 3 2 1
# 1 7 5 2 4