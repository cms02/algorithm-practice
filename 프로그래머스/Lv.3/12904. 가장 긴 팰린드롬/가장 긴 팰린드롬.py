def solution(s):
    answer = 1
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            # 문자열의 길이가 현재 저장된 문자열의 길이보다 짧으면 break
            # 어느 순간, j - i 가 변경되지 않아도 그냥 answer보다 짧아지는 경우도 break로 연산을 막는다
            if j - i < answer: 
                break
                        
            if s[i:j] == s[i:j][::-1]:
                answer = j - i
                break
            

    return answer