def quick_sort(array):
    if len(array) <=1:
        return array
    pivot = array[0]
    less = [x for x in array if x < pivot]
    
    equal = [x for x in array if x == pivot]
    
    great = [x for x in array if x > pivot]
    
    return quick_sort(less) + equal + quick_sort(great)

print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))