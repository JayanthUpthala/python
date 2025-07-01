def happy(n):
    s=0
    temp=n
    while True:
        while n>0:
            r=n%10
            s=s+r*r
            n=n//10
        if s==temp:
            return False
        if s==1:
            return True
        n=s
        s=0
    return False
print('Started Execution...')
assert happy(13)==True
print('Execution completed.')