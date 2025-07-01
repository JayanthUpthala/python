def uglynumber(n):
    if n>0:
        if n%2==0 or n%3==0 or n%5==0:
            return True
        else:
            return False
    else:
        return False
print('Execution started...')
assert uglynumber(-4)==False
assert uglynumber(6)==True
print('U r genius Yaar.')