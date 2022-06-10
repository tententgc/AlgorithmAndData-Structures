arr = [2,4,5,5,5,5,5,7,9,9]
target = 5
def fl1(arr,target):
    for i in range(len(arr)): 
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1] == target: 
                i+=1
            return  [start,i]
    return [-1,-1] 

print(fl1(arr,target))