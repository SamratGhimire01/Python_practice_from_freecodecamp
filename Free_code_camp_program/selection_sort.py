def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i
        j=i+1
        while j < len(array):
            if array[j] < array[min_index]:
                min_index = j
            j+=1
        if min_index != i:
            temp = array[i]
            array[i]=array[min_index]
            array[min_index]=temp

    return array

print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))
