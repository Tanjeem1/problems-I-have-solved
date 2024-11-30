a=int(input("take a random number: "))
x=0
for i in range (0,a+1):
   if 2**x<a:
       x+=1
z=x-1
print(((2**z-1)*x)+((a-2**z)+1)+(a-2**z))