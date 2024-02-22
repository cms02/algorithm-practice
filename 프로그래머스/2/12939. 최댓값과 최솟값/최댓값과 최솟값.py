def solution(s):
#     arr = list(map(int, s.split(' ')))
#     arr.sort()
        
#     return str(arr[0]) + ' ' + str(arr[-1])
    arr = list(map(int, s.split(' ')))
    return str(min(arr)) + ' ' + str(max(arr))