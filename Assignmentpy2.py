def matrix_chain_multiplication(dimensions):
    n = len(dimensions)
    m = [[0] * n for _ in range(n)]
    parenthesization = [[0] * n for _ in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    # Chain length
    for chain_len in range(2, n):
        for i in range(1, n - chain_len + 1):
            j = i + chain_len - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dimensions[i - 1][0] * dimensions[k][1] * dimensions[j][1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    parenthesization[i][j] = k
    # Get the optimal parenthesization
    def get_optimal_parenthesization(i, j):
        if i == j:
            return f'M{str(i)}'
        else:
            k = parenthesization[i][j]
            left_chain = get_optimal_parenthesization(i, k)
            right_chain = get_optimal_parenthesization(k + 1, j)
            return f'({left_chain} x {right_chain})'

    optimal_parenthesization = get_optimal_parenthesization(1, n - 1)

    return optimal_parenthesization, m[1][n - 1]
dimensions = [(9, 8), (5, 4), (1, 2)]
optimal_parenthesization, min_scalar_multiplications = matrix_chain_multiplication(dimensions)
print("Optimal Parenthesization:", optimal_parenthesization)
print("Minimum Scalar Multiplications:", min_scalar_multiplications)

