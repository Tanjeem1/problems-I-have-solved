

print('')
print('')
print('')

print('                                                                BRESERHAMS CIRCLE DRAW ALGORITHOM')

p=int(input('take value of p : '))
q=int(input('take value of q : '))
r=int(input('input the radious: '))
a=[0]
b=[r]
print('')
print('')
print('')
print('')

print(' The initial value of "x" is 0 \n Radious is',r,
      '\n The initial value of "y" is same as radious',r)
x=0
y=y1=r
d=1-r
x1=1
d1=0


for i in range (0,r,1):
      if d>=0:
            if (x1 < y1) or (x1 != y1):
                                      d1=d+2*x1+1-2*y1
                                      d = d1
                                      x=x1
                                      a.append(x)
                                      x1=x+1
                                      y=y1-1
                                      b.append(y)
                                      y1=y
            if (x1>y1) or (x1==y1):
                break

      if d<0:
            if (x1 < y1) or (x1 != y1):

                  d1 = d + 2 * x1 + 1
                  d = d1
                  x=x1
                  a.append(x)
                  x1=x+1
                  y=y1
                  b.append(y)
                  y1 = y


            if (x1>y1) or (x1==y1):
                break


for i,j in zip (a,b) :
    print('x,y: ',p+i,',',q+j)

print(' ')
print(' ')

for i,j in zip (a,b) :
    print('-x,y: ','-',p+i,',',q+j)

print(' ')
print(' ')

for i,j in zip (a,b) :
    print('x,-y: ',p+i,',','-',q+j)

print(' ')
print(' ')

for i,j in zip (a,b) :
    print('-x,-y: ','-',p+i,',','-',q+j)