N = int(input())
a = list(map(int, input().split()))
ave = int((sum(a) / N) + 0.5)
# round는 round_half_even 방식을 택함.
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
