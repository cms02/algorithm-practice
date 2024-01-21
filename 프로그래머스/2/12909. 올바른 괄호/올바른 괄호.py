def solution(s):
    answer = True
    stack = []
    for b in s:
        if b == '(':
            stack.append(b)
        elif len(stack) and b == ')':
            stack.pop()
        else:
            return False
    if len(stack):
        return False

    return answer