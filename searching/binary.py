# def binary_search(search_item, search_array, left_index, right_index):

#     mid = (right_index + left_index) // 2

#     if search_item == array[mid]:
#         return True
    
#     if (left_index >= right_index):
#         return False 

#     if search_item < array[mid]:
#         return binary_search(search_item, array, left_index, mid)
#     else:
#         return binary_search(search_item, array, mid+1, right_index)

'''Binary Search with less argument'''

def binary_search(search_item, search_array):
    left_index = 0
    right_index = len(search_array)-1
    mid = (right_index - left_index) // 2

    if search_item == search_array[mid]:
        return True
    
    if left_index >= right_index:
        return False

    if search_item < search_array[mid]:
        return binary_search(search_item, search_array[left_index: mid])
    else:
        return binary_search(search_item, search_array[mid+1: right_index+1])
    

array = [0,1,2,3,4,5,6,7,8]
# print(binary_search(search_item=int(input()),
#                     search_array=array,
#                     left_index=0,
#                     right_index=len(array)-1
#                     ))

print(binary_search(search_item=int(input()),
                    search_array=array))