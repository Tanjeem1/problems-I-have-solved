
def quicksort (arr, low,high):

    if low<high:
        pi=partition(arr, low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,low+1,high)

def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high, 1):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

arr=[100,34,23,11,55,44,22,76,88,44,22,11]
print("before sorted: ", arr)
print("")
quicksort(arr,0,len(arr)-1)
print("after sorted: ",arr)