def merge_sort(array, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(array, l, mid)
        merge_sort(array, mid+1, r)
        merge(array, l, mid, r)

def merge(array, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = array[left + i]

    for i in range(0, n2):
        R[i] = array[middle + 1 + i]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


arr = [3,2,1,4]
merge_sort(arr, l=0, r=len(arr)-1)
print(arr)