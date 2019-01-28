#name:prajwal dhore 
#div: p
# batch : b1
x=int(input('enter number of seconds'))
q1=x//86400
r1=x%86400
q2=r1//3600
r2=r1%3600
q3=r2//60
r3=r2%60
print('the number of days',q1,'number of hours',q2,'number of mins',q3,'number of seconds',r3)
