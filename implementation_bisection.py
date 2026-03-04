def square_root_bisection(number,tolerance = 0.1,max_iteration=10):
    if number <0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    low = 0
    high = max(1,number)
    root = None
    for i in range(max_iteration):
        mid = (low+high)/2
        if mid**2 <number:
            low = mid
        else:
            high = mid
        if (high - low) <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid
    print(f"Failed to converge within {max_iteration} iterations")
    return None
    
s= square_root_bisection(0.001, 1e-7, 50)