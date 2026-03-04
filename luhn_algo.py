def verify_card_number(array):
    array=array.replace("-", "").replace(" ", "")
    num = list(array)
    for i in range(len(num)-2,-1,-2):
        num[i] = int(num[i])*2
        if num[i] > 9:
            num[i] -=9
    add=0
    for i in range(len(num)):
        add+=int(num[i])
    print(add)
    if add%10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
    

print(verify_card_number('4111-1111-1111-1111'))