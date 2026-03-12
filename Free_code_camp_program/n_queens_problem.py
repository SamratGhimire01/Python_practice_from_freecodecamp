def dfs_n_queens(n):
    if n<1:
        return []
    solution = []
    stack = []
    stack.append([])
    while stack:
        current_board=stack.pop()
        if len(current_board)==n:
            solution.append(current_board)
        else:
            row = len(current_board)
            for col in range(n):
                is_safe = True
                for prev_row, prev_col in enumerate(current_board):
                    if prev_col == col or abs(row - prev_row) == abs(col - prev_col):
                        is_safe = False
                        break
                
                if is_safe:
                    stack.append(current_board + [col])
    return sorted(solution)

print(dfs_n_queens(5))