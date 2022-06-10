arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
target = 5
def find_end(arr, target): 
    if arr[-1] == target: 
        return len(arr) - 1 
    left, right = 0, len(arr)-1 
    while left <= right: 
        mid  = (left+right)//2 
        if arr[mid] == target and arr[mid+1] > target: 
            return mid 
        elif arr[mid] < target: 
             left = mid+1
        else: 
            right = mid - 1 
            
    return -1 
print(find_end(arr, target)) 