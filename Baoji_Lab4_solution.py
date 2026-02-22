def binary_research(matrix, k) :
    def bin_row(row, k):
        if len(row) == 0:
            return None

        m = len(row) // 2
        if k == row[m]:
            return m
        elif row[m] < k:
            idx = bin_row(row[m+1:], k)
            if idx is None:
                return None
            return m+1+idx
        else: return bin_row(row[:m], k)

    
    for row in matrix:
        if len(row) == 0:
            continue

        if k < row[0] or k > row[-1]:
            continue

        if bin_row(row, k) is not None:
            return True

    return False


matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]
print(binary_research(matrix, 5))   # True
print(binary_research(matrix, 20))  # False
print(binary_research(matrix, 1))   # True
print(binary_research(matrix, 30))  # True
print(binary_research(matrix, -1))  # False