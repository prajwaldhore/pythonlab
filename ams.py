x=int(input(' enter the number  ' ))
p=(x//10)
q=(x%10)
s=(p//10)
r=(p%10)
z=(s**3+q**3+r**3)
if     x==z:
       print('amstrong')
else:
       print('not')   
