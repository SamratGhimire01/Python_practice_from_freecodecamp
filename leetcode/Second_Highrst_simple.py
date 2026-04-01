def second_largest(data):
    largest  = second = -1
    
    for i in data:
        if i > largest:
            second = largest
            largest = i
        elif i>second and i<largest:
            second = i
    if second == largest:
        return -1
    return second

    
print(second_largest(  [12, 35, 1, 10, 34, 1]))
