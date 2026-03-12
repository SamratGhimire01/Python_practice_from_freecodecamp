def hanoi_solver(num):
    move = pow(2, num) - 1
    first = [x for x in range(num, 0, -1)]
    second = []
    third = []
    res = [f"{first} {second} {third}"]

    s, t = (second, third) if num % 2 != 0 else (third, second)
    
    i = 1
    while i <= move:
        if i % 3 == 1:
            if not t or (first and first[-1] < t[-1]):
                t.append(first.pop())
            else:
                first.append(t.pop())
        elif i % 3 == 2:
            if not s or (first and first[-1] < s[-1]):
                s.append(first.pop())
            else:
                first.append(s.pop())
        elif i % 3 == 0:
            if not t or (s and s[-1] < t[-1]):
                t.append(s.pop())
            else:
                s.append(t.pop())
        
        res.append(f"{first} {second} {third}")
        i += 1

    return "\n".join(res)
