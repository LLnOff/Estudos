x= int(input('digite um numero'))
y= int(input('digite um numero'))
if(x>y):
    y=y+1
    while(x>y):
        x=x-1
        print(x)
else:
    y=y-1
    while(x<y):
        x=x+1
        print(x)
