'''Selection Sort without Recurssion'''
def selection_sort(array):
    length = len(array)
    for start_pos  in range(length):
        min_pos = start_pos
        for search_pos in range(start_pos+1,length):
            if array[search_pos] < array[min_pos]:
                min_pos = search_pos
        (array[start_pos], array[min_pos]) = array[min_pos], array[start_pos]

'''Selection Sort with Recurssion'''
def rec_selection_sort(array, start_pos):
    length = len(array)
    if start_pos >= length:
        return
    min_pos = start_pos
    for i in range(start_pos, len(array)):
        if array[i] < array[min_pos]:
            min_pos = i

    (array[start_pos], array[min_pos]) = array[min_pos], array[start_pos]
    
    rec_selection_sort(array, start_pos+1)



a = [4,2,6,8,3,1,9,0]
rec_selection_sort(a, 0)
print(a)