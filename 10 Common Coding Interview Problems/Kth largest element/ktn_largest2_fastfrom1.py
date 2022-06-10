arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k = 4

def kth_largest(arr,k ): 
    n = len(arr)
    arr.sort()
    return arr[n-k]

print(kth_largest(arr, k)) 
#T(n,k) = O(nlogn ) + O(1) = O(nlogn)
