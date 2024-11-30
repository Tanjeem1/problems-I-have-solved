import re
import keyword

print("Enter a text: ", end="")
a=input([]).split()
b=keyword.kwlist

for i in a:
    if re.match("[0-9]",i[0]):
        print(i,"=","its not valid, because digit as the 1st character")
    if i not in b and re.match("^[A-za-z_][a-zA-Z_0-9]*$",i):
                print(i,"=","it's valid identifier")
    if i in b:
        print(i,"=","it's a keyword")
    x=re.match("[!@#$%6&\|'-,_={}:;'/+?.><,$]",i)
    if x:
            print (i,"=", "there is a special symbol in this word")


#(bool(re.match ("^[!@#$%6&*90-_=+{}:;'/?.><,]*$",i))==False)