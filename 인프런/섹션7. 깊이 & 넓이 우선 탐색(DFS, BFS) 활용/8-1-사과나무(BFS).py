n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
sum = 0
for i in range(n):
      if i<= n//2:
        for j in range(n//2-i,n//2+i+1):
          sum += a[i][j]
      else:
        for j in range(i-n//2, n-i//2):
          sum += a[i][j]
print(sum)





# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19