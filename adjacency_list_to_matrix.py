def adjacency_list_to_matrix(lists):
    length = len(lists)
    am= [[0 for _ in range(length)] for _ in range(length)]
    
    for i in range(length):
        data = lists[i]
        for j in range(length):
            if not j in data:
                am[i][j]=0
            else:
                am[i][j]=1
    for i in am:
        print(i)
    return am

adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]})