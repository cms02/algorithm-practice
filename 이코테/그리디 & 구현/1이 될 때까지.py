#<문제> 1이 될 때까지

# 내 답안
n, k = map(int, input().split())
count = 0
while True:
    if (n == 1):
        break

    if (n % k == 0):
        n = n // k
    else:
        n = n - 1
    count += 1
print(count)

#모범 답안
# N, K를 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n - 1)
print(result)
