n = int(input())
body = []
for _ in range(n):
    h, w = map(int, input().split())
    body.append((h, w))

body.sort(reverse=True)

cnt = 0
largest = 0
for h, w in body:
    if w > largest:
        largest = w
        cnt += 1
print(cnt)
