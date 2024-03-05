def solution(n):
    answer = []
    hanoi(n,1,3,2, answer)
    return answer



def hanoi(n, from_pos, to_pos, aux_pos, answer):
    if n == 1:  
        answer.append([from_pos, to_pos])
    else:
        hanoi(n-1, from_pos, aux_pos, to_pos, answer)
        hanoi(1, from_pos, to_pos, aux_pos, answer)
        hanoi(n-1, aux_pos, to_pos, from_pos, answer)