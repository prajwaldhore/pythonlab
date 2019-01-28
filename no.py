d={}
x=int(input('enter no. of students  '))
for i in range(x):
    print('profile student no.  ' ,i+1)
    n=input('name')
    g=int(input('gr'))
    b=input()
    d[g]=(n,b)
print(d)
