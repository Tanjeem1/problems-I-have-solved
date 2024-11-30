print('')
print('')
print('')
print('')
print('')

print('                                                                BRESERHAMS CIRCLE DRAW ALGORITHOM')


a=[0]
b=[8]
print('')
print('')
print('')
print('')

r=int(input('input the radious: '))
print(' ')

print(' The initial value of "x" is 0 \n Radious is',r,
      '\n The initial value of "y" is same as radious',r)
x=0
y=y1=r
d=3-2*r
x1=1
d1=0


for i in range (0,r,1):
      if d>=0:
            if (x1 < y1) or (x1 != y1):
                                      d1=d+4*(x1-y1)+10
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

                  d1 = d + 4 * x1 + 6
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
    print('x,y: ',i,',',j)

print(' ')
print(' ')

for i,j in zip (a,b) :
    print('-x,y: ','-',i,',',j)

print(' ')
print(' ')

for i,j in zip (a,b) :
    print('x,-y: ',i,',','-',j)

print(' ')
print(' ')

for i,j in zip (a,b) :
    print('-x,-y: ','-',i,',','-',j)