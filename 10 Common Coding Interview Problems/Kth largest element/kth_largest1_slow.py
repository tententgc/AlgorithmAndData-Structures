arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k = 4


def kth_largest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)


print(kth_largest(arr, k))

#T(n,k) = 2kn-n = O(kn)
#S(n,k) = O(1)