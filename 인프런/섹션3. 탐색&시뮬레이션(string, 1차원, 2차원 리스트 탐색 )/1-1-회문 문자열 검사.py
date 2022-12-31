n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = s.len()
    for j in range(size // 2):
        if s[j] != s[-1 - j]:
            print("#%d NO" % (i + 1))
            break
    else:
        print("#%d YES" % (i + 1))
