def dfs(adj_mat,num):
    stack=[]
    visited = []
    result = []

    stack.append(num)
    visited.append(num)
    while stack:
        current_node=stack.pop()
        result.append(current_node)
        for neb,is_connect in enumerate(adj_mat[current_node]):
            if is_connect == 1 and neb not in visited:
                visited.append(neb)
                stack.append(neb)
    return result



print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))