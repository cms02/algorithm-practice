str = input()
for x in str:
    if x.isupper():
        print(x.lower(), end='')
    else:
        print(x.upper(), end ='')