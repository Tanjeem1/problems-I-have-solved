mport sys
print("")
print("")
print("")
print("                                                        Adoptive Decision Boundary Coding        ")
print("")
print("")
print("")


old_w0=old_w1=0
c=1
k=1
print("Enter that how many times you want to run the iteration")
n=int(input("Enter: "))
print("")

for i in range (0,n,1):
    print("enter value of x & d for iteration: ",i+1)
    x=int(input("enter value of x: "))
    d= int(input("enter value of d: "))
    print(" ")
    print("after calculating the value of D, new_w0, new_w1 the result is....")
    D=old_w0+old_w1*x
    print("value of D is : ",D)


    if (d < 0 and D < 0) or (d>0 and D>0):
        new_w1=old_w1
        old_w1 = new_w1
        print("value of new w1 is: ", new_w1)
        new_w0= old_w0
        old_w0 = new_w0
        print("value of new w0 is: ", new_w0)
        print("")
        print("")
        print("process of iteration ", "(", i + 1, ")", "is Correct & there is no Error.")

        
    else:
        print("")
        new_w0 = old_w0 + c * d * k
        old_w0=new_w0
        print("value of new w0 is: ", new_w0)
        new_w1 = old_w1 + c * d * x
        old_w1=new_w1
        print("value of new w1 is: ", new_w1)
        print("")
        print("")
        print("process of iteration ", "(", i + 1, ")", "is not Correct & there is an Error.")
    print("")
    print("")
    print("")

    if n>1 and i<n:
         print("                                        ........Another New Process Is Beginning.......")
         print("")
         print(" ")
    else:
        sys.exit()





