def number_pattern(n):
    if not isinstance(n,int):
        return 'Argument must be an integer value.'
    if n<=0:
        return 'Argument must be an integer greater than 0.'
    sum=[]
    for i in range(n):
        sum.append(str(i+1))
    return " ".join(sum)

print(number_pattern(12))
