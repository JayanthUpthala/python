import math
def palindrome(n):
    s=str(n)
    return s==s[::-1]

def prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,n,2):
        if n%i==0:
            return False
    return True

def palindromic_prime(n):
    return palindrome(n) and prime(n)

print('Hey...')
assert palindromic_prime(11)==True
print('Urgent ga US vellipo sivaji...')