T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = l[s - 1:e]
    l.sort()
    print(l[k - 1])
