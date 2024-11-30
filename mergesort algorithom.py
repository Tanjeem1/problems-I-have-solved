def mergesort(arr):
    if len(arr)>1:
        leftarray=arr[:len(arr)//2]
        rightarray=arr[len(arr)//2:]

        mergesort(leftarray)
        mergesort(rightarray)
        merge (arr,leftarray,rightarray)
        
def merge(arr,leftarray, rightarray):
        i=j=k= 0
        while i< len(leftarray) and j<len(rightarray):
             if leftarray[i] < rightarray[j]:
                 arr[k]= leftarray[i]
                 i+=1
             else:
                 arr[k]= rightarray[j]
                 j+=1
             k+=1
        while i < len(leftarray):
             arr[k]=leftarray[i]
             i+=1
             k+=1
        while j < len(rightarray):
             arr[k]=rightarray[j]
             j+=1
             k+=1


testarr =[int(x) for x in input("Enter the elements separated by space: ").split()]
print('before sorting: ', testarr)
print('')
mergesort(testarr)
print('after sorting: ',testarr)
