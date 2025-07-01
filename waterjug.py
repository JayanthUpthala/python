x=int(input('Enter X: '))
y=int(input('Enter Y: '))
while True:
    rn=int(input('Enter rule No...: '))
    if rn==1:
        if x<=4:x=4
    if rn==2:
        if y<=3:y=3
    if rn==5:
        if x>=0:x=0
    if rn==6:
        if y>=0:y=0
    if rn==7:
        if x+y>=4:x,y=4,y-(4-y)
    if rn==8:
        if x+y>=3:x,y=x-(3-y),3
    if rn==9:
        if x+y<=4:x,y=x+y,0
    if rn==10:
        if x+y>=3:x,y=0,x+y-3
    print('X= ',x)
    print('Y= ',y)
    if x==2:
        print('Reached Goal State')
        break