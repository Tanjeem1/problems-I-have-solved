import numpy as np

nums=np.array([5,2,99,3,4,1,100])
a=np.sort(nums)
b=max(np.split(a,np.where(np.diff(a)!=1)[0]+1), key=len).tolist()
print(b)
'''''''''
np.where(np.diff(nums) != 1)[0]+1 -gets the indices of elements on which the array should be split 
(if difference between 2 consequtive numbers is not equal to 1, e.g. 3 and 5)

np.split(...) - split the array into sub-arrays
'''''''''''
