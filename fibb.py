
n=int(input("Enter a number: "))
n1=0
n2=1
print("0 1", end=" ")
for i in range(n-2):
    n3 = n1 + n2
    print(n3, end=" ")
    n1 = n2
    n2 = n3
print()
# def fibrec(a, b):
#     if(n==1):
#         return 1
#     else:
        
    