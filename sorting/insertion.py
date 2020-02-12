def insertion(array):
    for index in range(1, len(array)):
        min_pos = index
        while(min_pos > 0 and array[min_pos] < array[min_pos - 1]):
            array[min_pos], array[min_pos-1] = array[min_pos - 1], array[min_pos]
            min_pos -= 1


unsorted_array = [5,4,3,2,1,0]
insertion(unsorted_array)
print(unsorted_array)