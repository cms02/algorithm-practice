a = input()
stack = []
res = 0
for x in a:
  if x.isdecimal():
    stack.append(x)
  else:
    if x == '+':
        res = int(stack.pop(-2)) + int(stack.pop(-1))
        stack.append(res)
    elif x == '-':
        res =  int(stack.pop(-2)) - int(stack.pop(-1))
        stack.append(res)
    elif x == '*':
        res = int(stack.pop(-2)) * int(stack.pop(-1))
        stack.append(res)
    elif x == '/':
        res = int(stack.pop(-2)) / int(stack.pop(-1))
        stack.append(res)
print(res)
        
      