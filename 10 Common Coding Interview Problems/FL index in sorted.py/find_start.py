arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
target = 5
def find_start(arr,target): 
    if arr[0]==target:
        return 0
    left,right = 0,len(arr)-1 
    while left <= right:
        mid = (left+right)//2 
        if arr[mid] == target and arr[mid-1] < target: 
            return mid
        elif arr[mid] < target: 
            left = mid+1 
        else: 
            right = mid - 1 
    
find_start(arr,target) 