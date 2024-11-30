def get_subsets(array):
    print("take an array list:")
    array=input([])
    a=len(array)
    subsets=[]
    for i in range (2**a):
        b=bin(i)[2:].zfill(a)
        subset=[]
        for j in range (a):
            if b[j]=="1":
                subset.append(array[j])
        subsets.append(subset)
    return print((subsets))

array=""
get_subsets(array)