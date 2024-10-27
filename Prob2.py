##################################################
# Name: Gabriella Weis
# Collaborators:
# Estimate of time spent (hr): 1
##################################################

def is_magic_square(array:list[list[int]]) -> bool:
    n = len(small)
    for row in small:
        if n == 0 or len(row) != n:
            return False
        
    # sum that all other rows, columns, and diagonals must match
    magic_sum = sum(small[0])

    # rows
    for row in small:
        if sum(row) != magic_sum:
            return False
    
    # columns
    for col in range(n):
        if sum(small[row][col] for row in range(n)) != magic_sum:
            return False
            
    # left diagonal
    if sum(small[i][i] for i in range(n)) != magic_sum:
        return False

    # right diagonal
    if sum(small[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False
    
    # no conditions are met
    return True

small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))
